from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.FlatCreateView.as_view(), name='create'),
    path('chaining/', include('smart_selects.urls')),
]