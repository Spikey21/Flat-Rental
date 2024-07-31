from django.core.mail import send_mail
from django.db.models.signals import post_save, pre_save, m2m_changed
from notifications.signals import notify
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _

from .models import Notification, NotificationType
from flat.models import Flat, FlatDetail, FlatLocation
from message.models import Chat, Message


@receiver(post_save, sender=Flat)
def create_flat(sender, created, instance, update_fields, **kwargs):
    if created:
        # Send a notification
        notify.send(instance, recipient=instance.user, notification_type=NotificationType.objects.filter(name='Add').first(), verb=_("New flat showed up!"), message=_("You have new flat in your preferences"))


@receiver(post_save, sender=Chat)
def create_chat(sender, created, instance, update_fields, **kwargs):
    if created:
        users = instance.participants.all()
        for user in users:
            # Send a notification
            notify.send(instance, recipient=user, notification_type=NotificationType.objects.filter(name="Add").first(), verb=_("New Chat showed up!"), message=_("Some is trying to reach you!"))


@receiver(post_save, sender=Message)
def send_message(sender, created, instance, update_fields, **kwargs):
    if created:
        # Send a notification
        notify.send(instance, recipient=instance.chat.participants, notification_type=NotificationType.objects.filter(name="Add").first(), verb=_(f"New message from {instance.user}!"), message=_("You have new messages in your chat"))


@receiver(m2m_changed, sender=Chat.participants.through)
def chat_users_changed(sender, instance, action, **kwargs):
    if action == "post_add":
        users = instance.participants.all()
        for user in users:
            Notification.objects.create(
                recipient=user,
                notification_type=NotificationType.objects.filter(name="Add").first(),
                verb=_(f"New message from {instance.user}!"),
                message=f"A new Chat '{instance.name}' was added.",
            )


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


@receiver(pre_save, sender=FlatDetail)
def notify_update_flat(sender, instance, **kwargs):
    if instance.pk:  # Only check if the instance already exists (i.e., is being updated)
        try:
            old_instance = FlatDetail.objects.get(pk=instance.pk)
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
            notify.send(instance, recipient=instance.flat.user,
                        notification_type=NotificationType.objects.filter(name="Mod").first(),
                        verb=_("Flat has been updated"), message=_("Fields updated: \n" +
                                                                   '\n'.join("{}: {}".format(k, v) for k, v in changed_fields.items())))


@receiver(pre_save, sender=FlatLocation)
def notify_update_flat(sender, instance, **kwargs):
    if instance.pk:  # Only check if the instance already exists (i.e., is being updated)
        try:
            old_instance = FlatLocation.objects.get(pk=instance.pk)
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
            notify.send(instance, recipient=instance.flat.user,
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
