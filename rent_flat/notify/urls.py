from django.urls import path, include
from . import views
import notifications.urls


urlpatterns = [
    path('inbox/notifications/', include(notifications.urls, namespace='notifications')),
]