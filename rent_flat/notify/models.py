from django.db import models
from django.conf import settings

from notifications.models import Notification as BaseNotification

User = settings.AUTH_USER_MODEL


class NotificationType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Notification(BaseNotification):
    notification_type = models.ForeignKey(NotificationType, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    message = models.CharField(max_length=200)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.message
