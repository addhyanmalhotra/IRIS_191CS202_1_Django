from django.contrib import admin
from .models import *
from datetime import date
from datetime import timedelta


# Register your models here.
class BIAdmin(admin.ModelAdmin):
    readonly_fields = ['available']

    def save_model(self, request, obj, form, change):
        if not change:
            book = form.cleaned_data['ISBN']
            book.Quantity += 1
            book.InStock += 1
            book.save()
        super().save_model(request, obj, form, change)

    def delete_model(self, request, obj):
        book = obj.ISBN
        book.Quantity -= 1
        book.InStock -= 1
        book.save()
        super(BIAdmin, self).delete_model(request, obj)


class BookAdmin(admin.ModelAdmin):
    readonly_fields = ['Quantity']


class RequestAdmin(admin.ModelAdmin):
    # readonly_fields = ['borrower', 'book']
    actions = ['approve_requests', 'reject_requests']
    list_filter = ("isApproved", "borrower", "book")

    def approve_requests(self, request, queryset):
        for rq in queryset:
            bkinstance = rq.book
            bk = rq.book.ISBN
            bk.InStock -= 1
            bk.save()
            # create transaction
            tr = Transactions(IssueDate=date.today(), DueDate=date.today() + timedelta(days=7), Request=rq)
            tr.save()
            bkinstance.available = False
            bkinstance.last_transaction = tr
            bkinstance.save()
        queryset.update(isApproved=1)

    def reject_requests(self, request, queryset):
        queryset.update(isApproved=2)


admin.site.register(BookInstance, BIAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(IssueRequest, RequestAdmin)
admin.site.register(Transactions)
