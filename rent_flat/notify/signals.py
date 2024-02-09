from django.db.models.signals import post_save
from notifications.signals import notify
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _

from flat.models import Flat
from .models import Notification, NotificationType


@receiver(post_save, sender=Flat)
def create_flat(sender, created, instance, update_fields, **kwargs):
    if created:
        notify.send(instance, recipient=instance.user, verb=_("You have new flat"))