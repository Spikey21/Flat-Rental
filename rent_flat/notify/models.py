from django.db import models
from django.conf import settings

from notifications.base.models import AbstractNotification

from .const import NotifyType

User = settings.AUTH_USER_MODEL


class NotificationType(models.Model):
    name = models.CharField(choices=NotifyType.choices(),max_length=100)

    def __str__(self):
        return self.name


class Notification(AbstractNotification):
    notification_type = models.ForeignKey(NotificationType, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    message = models.CharField(max_length=200)

    class Meta:
        abstract = False
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.message}"