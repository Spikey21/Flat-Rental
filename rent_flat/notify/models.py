from django.db import models
from django.conf import settings

from notifications.models import Notification as BaseNotification

User = settings.AUTH_USER_MODEL


class NotificationType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Notification(BaseNotification):
    recipient = models.ForeignKey(User, on_delete=models.CASCADE)
    notification_type = models.ForeignKey(NotificationType, on_delete=models.CASCADE)
    # Additional fields specific to your notification

    class Meta:
        ordering = ['-timestamp']