from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView
from django.contrib.auth.mixins import LoginRequiredMixin
from user_profile.forms import UserRegisterForm
from django.views.generic.edit import CreateView
from django.contrib.auth import login, authenticate
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy




class MyLoginView(LoginView):
    template_name = 'registration/login.html'

class MyLogOutView(LogoutView):
    template_name = 'registration/logout.html'

class CreateUserView(CreateView):
    template_name = 'registration/usercreate.html'
    success_url = reverse_lazy('profile:user_update')
    form_class = UserRegisterForm
    success_message = "Профиль был создан успешно"

    def form_valid(self, form):
        form.save()
        username = self.request.POST['username']
        password = self.request.POST['password1']
        user = authenticate(username=username, password=password)
        login(self.request, user)
        return HttpResponseRedirect(reverse_lazy('profile:user_profile'))
