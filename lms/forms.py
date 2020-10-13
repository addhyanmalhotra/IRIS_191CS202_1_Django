from django import forms
from .models import *


class BookUploadForm(forms.ModelForm):
    class Meta:
        model = BookInstance
        fields = "__all__"
        exclude = ['IssueDate', 'DueDate', 'Borrower']
