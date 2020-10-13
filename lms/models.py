from django.db import models
from django.contrib.auth.models import User


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

    def __str__(self):
        return self.ISBN.BookTitle


class IssueRequest(models.Model):
    borrower = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    book = models.ForeignKey('BookInstance', on_delete=models.DO_NOTHING)
    isApproved = models.IntegerField(default=0, choices=[(0, 'Pending'), (1, 'Approved'), (2, 'Rejected')])

    def __str__(self):
        return "NITK-IR0"+str(self.pk)


class Transactions(models.Model):
    IssueDate = models.DateField()
    DueDate = models.DateField()
    Request = models.ForeignKey('IssueRequest', on_delete=models.RESTRICT)
    isReturned = models.BooleanField(default=False)

    def __str__(self):
        return "NITK-TR0"+str(self.pk)
