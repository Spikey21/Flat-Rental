from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.FlatCreateView.as_view(), name='create'),
    path('flats/', views.FlatListView.as_view(), name='flats'),
    path('flat/<int:pk>/', views.FlatDetailView.as_view(), name='detail'),
    path('chaining/', include('smart_selects.urls')),
]