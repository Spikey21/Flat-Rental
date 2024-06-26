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
        # Send a notification
        notify.send(instance, recipient=instance.user, notification_type=NotificationType.objects.filter(name="Add").first(), verb=_("New flat showed up!"), message=_("You have new flat in your preferences"))


@receiver(pre_save, sender=Flat)
def notify_delete_flat(sender, instance, **kwargs):
    if instance.pk:  # Only check if the instance already exists (i.e., is being updated)
        try:
            old_instance = Flat.objects.get(pk=instance.pk)
        except Flat.DoesNotExist:
            return
        if old_instance.status != instance.status:  # Check if field updated
            # Send a notification
            notify.send(instance, recipient=instance.user,
                        notification_type=NotificationType.objects.filter(name="Del").first(),
                        verb=_("Status od flat has changed "), message=_("Flat in your preferences is no longer available"))


@receiver(pre_save, sender=Flat)
def notify_update_flat(sender, instance, **kwargs):
    if instance.pk:  # Only check if the instance already exists (i.e., is being updated)
        try:
            old_instance = Flat.objects.get(pk=instance.pk)
        except Flat.DoesNotExist:
            return
        changed_fields = {}
        for field in instance._meta.fields:
            field_name = field.name
            old_value = getattr(old_instance, field_name)
            new_value = getattr(instance, field_name)
            if old_value != new_value:
                changed_fields[field_name] = {
                    'old': old_value,
                    'new': new_value
                }

        if changed_fields:
            # Send a notification
            notify.send(instance, recipient=instance.user,
                        notification_type=NotificationType.objects.filter(name="Mod").first(),
                        verb=_("Flat has been updated"), message=_("Fields updated: \n" +
                                                                   '\n'.join("{}: {}".format(k, v) for k, v in changed_fields.items())))


@receiver(post_save, sender=Notification)
def send_email(sender, created, instance, update_fields, **kwargs):
    send_mail(
        f'{instance.verb}',
        f'{instance.message}',
        f'helpdesk@rent-flat.com',
        [f'{instance.recipient.email}'],
    )
