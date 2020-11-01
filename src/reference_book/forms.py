from django import forms
from . import models


class CreateGenreForm(forms.ModelForm):
    class Meta:
        model = models.Genre
        fields = '__all__'

class UpdateGenreForm(forms.ModelForm):
    class Meta:
        model = models.Genre
        fields = '__all__'
    genre_id = forms.CharField(widget=forms.HiddenInput)

    
class CreateAuthorForm(forms.ModelForm):
    class Meta:
        model = models.Author
        fields = '__all__'

class UpdateAuthorForm(forms.ModelForm):
    class Meta:
        model = models.Author
        fields = '__all__'
    author_id = forms.CharField(widget=forms.HiddenInput)

class CreateSerieForm(forms.ModelForm):
    class Meta:
        model = models.Serie
        fields = '__all__'

class UpdateSerieForm(forms.ModelForm):
    class Meta:
        model = models.Serie
        fields = '__all__'
    serie_id = forms.CharField(widget=forms.HiddenInput)

class CreatePublisherForm(forms.ModelForm):
    class Meta:
        model = models.Publisher
        fields = '__all__'

class UpdatePublisherForm(forms.ModelForm):
    class Meta:
        model = models.Publisher
        fields = '__all__'
    publisher_id = forms.CharField(widget=forms.HiddenInput)

