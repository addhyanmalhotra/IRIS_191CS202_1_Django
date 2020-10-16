from django.db import models
from django.contrib.auth.models import User
from datetime import date

# Create your models here.
class Book(models.Model):
    ISBN = models.CharField(max_length=13, unique=True)
    BookTitle = models.CharField(max_length=144)
    Description = models.TextField()
    Images = models.ImageField(upload_to='media/')
    Quantity = models.IntegerField(default=0)
    InStock = models.IntegerField(default=0)

    def __str__(self):
        return self.BookTitle


class BookInstance(models.Model):
    BookId = models.CharField(max_length=13, unique=True)
    ISBN = models.ForeignKey('Book', on_delete=models.CASCADE)
    Condition = models.IntegerField(choices=[(0, 'New'),
                                             (1, 'Good'),
                                             (2, 'Superficial Damage'),
                                             (3, 'Missing Pages')],
                                    default=0)
    available = models.BooleanField(default=True)
    Images = models.ImageField(upload_to='media/', blank=True, null=True)
    last_transaction = models.ForeignKey('Transactions', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        ordering = ['-available']

    def __str__(self):
        return self.ISBN.BookTitle


class IssueRequest(models.Model):
    borrower = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    book = models.ForeignKey('BookInstance', on_delete=models.DO_NOTHING)
    isApproved = models.IntegerField(default=0, choices=[(0, 'Pending'), (1, 'Approved'), (2, 'Rejected'), (3, 'Approved->Returned')])

    def __str__(self):
        return "NITK-IR0"+str(self.pk)


class Transactions(models.Model):
    IssueDate = models.DateField(default=date.today())
    DueDate = models.DateField(default=date.today())
    Request = models.ForeignKey('IssueRequest', on_delete=models.RESTRICT)
    isReturned = models.BooleanField(default=False)

    def __str__(self):
        return "NITK-TR0"+str(self.pk)
