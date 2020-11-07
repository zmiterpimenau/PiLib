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


    
class CreateAuthorForm(forms.ModelForm):
    class Meta:
        model = models.Author
        fields = '__all__'

class UpdateAuthorForm(forms.ModelForm):
    class Meta:
        model = models.Author
        fields = '__all__'

class CreateSerieForm(forms.ModelForm):
    class Meta:
        model = models.Serie
        fields = '__all__'

class UpdateSerieForm(forms.ModelForm):
    class Meta:
        model = models.Serie
        fields = '__all__'


class CreatePublisherForm(forms.ModelForm):
    class Meta:
        model = models.Publisher
        fields = '__all__'

class UpdatePublisherForm(forms.ModelForm):
    class Meta:
        model = models.Publisher
        fields = '__all__'


