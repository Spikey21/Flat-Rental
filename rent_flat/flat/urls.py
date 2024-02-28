from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.HomeListView.as_view(), name='home'),
    path('create/', views.FlatCreateView.as_view(), name='create'),
    path('flats/', views.FlatListView.as_view(), name='flats'),
    path('my-ads/', views.MyFlatListView.as_view(), name='my_ads'),
    path('flat/<int:pk>/', views.FlatDetailView.as_view(), name='detail'),
    path('update-flat/<int:pk>/', views.FlatUpdateView.as_view(), name='update'),
    path('chaining/', include('smart_selects.urls')),
]