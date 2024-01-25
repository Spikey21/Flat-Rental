from django.urls import path, include
from django.contrib.auth import views as auth_views

from . import views


urlpatterns = [
    path('login/', views.LogIn.as_view(), name='login'),
    path('logout/', views.LogOut.as_view(), name='logout'),
    path("signup/", views.SignUp.as_view(), name="signup"),
    path('account/', views.UserView.as_view(), name='profile'),
    path("account/change-password/", views.PasswordChange.as_view(), name="change_password"),
    path('account/change-password/done/', views.PasswordChangeDone.as_view(), name='change_password_done'),
    path('account/reset-password/', views.ResetPasswordView.as_view(), name='reset_password'),
    path('account/reset-password-confirm/<uidb64>/<token>/',
         views.ResetConfirmPasswordView.as_view(),
         name='reset_password_confirm'),
    path('account/reset-password-complete/', views.ResetCompletePasswordView.as_view(), name='reset_password_complete'),
    path("", include("django.contrib.auth.urls")),
]