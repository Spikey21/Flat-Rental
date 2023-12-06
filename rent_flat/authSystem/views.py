from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from rent_flat.authSystem.forms import CustomUserCreationForm


class LogIn(SuccessMessageMixin, LoginView):
    template_name = "login.html"

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, f'Welcome {self.request.user.username}')
        return response


class SignUp(SuccessMessageMixin, CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "signup.html"
    success_message = "Your account has been created. You can go ahead and log in now!"