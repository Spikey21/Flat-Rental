from django.urls import path, include
from django.contrib.auth import views as auth_views

from . import views


urlpatterns = [
    path('login/', views.LogIn.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path("signup/", views.SignUp.as_view(), name="signup"),
    path("account/change_password/", views.PasswordChange.as_view(), name="change_password"),
    path('account/reset_password/', views.ResetPasswordView.as_view(), name='reset_password'),
    path('account/reset-password-confirm/<uidb64>/<token>/',
         views.ResetConfirmPasswordView.as_view(),
         name='reset_password_confirm'),
    path('account/reset-password-complete/', views.ResetCompletePasswordView.as_view(), name='reset_password_complete'),
    path("", include("django.contrib.auth.urls")),
]