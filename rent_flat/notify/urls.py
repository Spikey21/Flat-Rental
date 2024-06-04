from django.urls import path, include
from . import views
import notifications.urls


urlpatterns = [
    path('inbox/notifications/', include(notifications.urls, namespace='notifications')),
    path('notifications/', views.NotificationListView.as_view(), name='notification_list'),
    path('inbox/notifications/<int:pk>/detail', views.NotificationDetailView.as_view(), name='notification_detail'),
]