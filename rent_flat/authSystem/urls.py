from django.urls import path, include
from django.contrib.auth import views as auth_views

from . import views


urlpatterns = [
    path('login/', views.LogIn.as_view(), name='login'),
    path("signup/", views.SignUp.as_view(), name="signup"),
]