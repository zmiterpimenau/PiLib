from django.shortcuts import render
from user_profile import forms
from user_profile import models
from django.views.generic import UpdateView, TemplateView, DetailView
from django.http import HttpResponseRedirect


class ProfileView(TemplateView):
    model = models.UserProfile
    template_name = 'user_profile/userprofile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        user = self.request.user
        profile = models.UserProfile.objects.filter(user=user).first()

        if user.first_name:
            profile.first_name = user.first_name

        if user.last_name:
            profile.last_name = user.last_name

        profile.email = user.email

        profile.save()

        context['profile'] = profile
        return context

class UpdateProfileView(UpdateView):
    model = models.UserProfile
    template_name = 'user_profile/userupdate.html'
    fields = (
        'first_name',
        'last_name',
        'email',
        'phone_number',
        'country',
        'city',
        'zip_code',
        'second_address',
        'third_address',
        'additional_information')
    success_url = '/profile'
