from django.contrib import messages
from django.contrib.auth import get_user_model, update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetConfirmView, \
    PasswordResetCompleteView, PasswordChangeDoneView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, FormView, DetailView

from .forms import CustomUserCreationForm


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


class LogOut(LoginRequiredMixin, SuccessMessageMixin, LogoutView):
    login_url = 'login'
    success_url = reverse_lazy("home")
    success_message = "Your account has been log out of the system."


class UserView(LoginRequiredMixin, DetailView):
    login_url = 'login'
    template_name = 'profile.html'

    def get_object(self, **kwargs):
        return self.request.user


class PasswordChange(LoginRequiredMixin, SuccessMessageMixin, FormView):
    login_url = 'login'
    model = get_user_model()
    form_class = PasswordChangeForm
    success_url = reverse_lazy("home")
    template_name = "account/change_password.html"
    success_message = "Password has been changed."

    def get_form_kwargs(self):
        kwargs = super(PasswordChange, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.save()
        update_session_auth_hash(self.request, form.user)
        return super(PasswordChange, self).form_valid(form)


class PasswordChangeDone(LoginRequiredMixin, SuccessMessageMixin, PasswordChangeDoneView):
    template_name = 'account/change_password_done.html'


class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    template_name = 'account/reset_password.html'
    email_template_name = 'account/reset_password_email.html'
    subject_template_name = 'account/reset_password_subject.txt'
    success_message = "We've emailed you instructions for resetting your password, " \
                      "if an account exists with the email you entered. You should receive them shortly. " \
                      "Please make sure you've entered the address you registered with, and check your spam folder."
    success_url = reverse_lazy("home")


class ResetConfirmPasswordView(SuccessMessageMixin, PasswordResetConfirmView):
    template_name = 'account/reset_password_confirm.html'
    success_url = reverse_lazy("reset_password_complete")
    success_message = "Password has been changed. You can go ahead and log in now."


class ResetCompletePasswordView(SuccessMessageMixin, PasswordResetCompleteView):
    template_name = 'account/reset_password_complete.html'

