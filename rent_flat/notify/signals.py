from django.core.mail import send_mail
from django.db.models.signals import post_save
from notifications.signals import notify
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _

from flat.models import Flat
from .models import Notification, NotificationType


@receiver(post_save, sender=Flat)
def create_flat(sender, created, instance, update_fields, **kwargs):
    if created:
        notify.send(instance, recipient=instance.user, notification_type=NotificationType.objects.filter(name="Add").first(), verb=_("You have new flat"), message=_("You have new flat"))


@receiver(post_save, sender=Flat)
def update_flat(sender, created, instance, update_fields, **kwargs):
    if update_fields:
        notify.send(instance, recipient=instance.user, notification_type=NotificationType.objects.filter(name=("Del" or "Mod")).first(), verb=_("Status has changed"), message=_("Status of flat has changed"))


@receiver(post_save, sender=Notification)
def send_email(sender, created, instance, update_fields, **kwargs):
    send_mail(
        f'{instance.verb}',
        f'{instance.message}',
        f'helpdesk@rent-flat.com',
        [f'{instance.recipient.email}'],
    )
