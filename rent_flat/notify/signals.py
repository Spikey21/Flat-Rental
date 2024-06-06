from django.core.mail import send_mail
from django.db.models.signals import post_save, pre_save
from notifications.signals import notify
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _

from flat.models import Flat
from .models import Notification, NotificationType


@receiver(post_save, sender=Flat)
def create_flat(sender, created, instance, update_fields, **kwargs):
    if created:
        notify.send(instance, recipient=instance.user, notification_type=NotificationType.objects.filter(name="Add").first(), verb=_("New flat showed up!"), message=_("You have new flat in your preferences"))


@receiver(pre_save, sender=Flat)
def on_change(sender, instance, **kwargs):
    if instance.id is None: # new object will be created
        pass # write your code here
    else:
        previous = Flat.objects.get(id=instance.id)
        if previous.title != instance.title: # field will be updated
            notify.send(instance, recipient=instance.user,
                        notification_type=NotificationType.objects.filter(name=("Del" or "Mod")).first(),
                        verb=_("Status od flat has changed"), message=_("Status has changed of your prefereneces"))

@receiver(post_save, sender=Flat)
def update_flat(sender, created, instance, update_fields, **kwargs):
    if update_fields:
        notify.send(instance, recipient=instance.user, notification_type=NotificationType.objects.filter(name=("Del" or "Mod")).first(), verb=_("Status od flat has changed"), message=_("Status has changed of your prefereneces"))


@receiver(post_save, sender=Notification)
def send_email(sender, created, instance, update_fields, **kwargs):
    send_mail(
        f'{instance.verb}',
        f'{instance.message}',
        f'helpdesk@rent-flat.com',
        [f'{instance.recipient.email}'],
    )
