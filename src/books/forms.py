from django import forms
from . import models


class CreateBookForm(forms.ModelForm):
    class Meta:
        model = models.Book
        fields = '__all__'
        widgets = {'book_name': forms.TextInput({"placeholder": "Введите название книги"})}

class UpdateBookForm(forms.ModelForm):
    class Meta:
        model = models.Book
        fields = '__all__'
