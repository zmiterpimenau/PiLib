from django import forms
from user_profile import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm



class ProfileForm(forms.ModelForm):
    class Meta:
        model = models.UserProfile
        fields = '__all__'

class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = models.UserProfile
        fields = '__all__'

class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = models.UserProfile
        fields = '__all__'

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']


