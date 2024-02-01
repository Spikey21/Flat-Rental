# Generated by Django 4.2.6 on 2024-02-01 23:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('notifications', '0009_alter_notification_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='NotificationType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('notification_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.NOTIFICATIONS_NOTIFICATION_MODEL)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('message', models.CharField(max_length=200)),
                ('notification_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='notify.notificationtype')),
            ],
            options={
                'ordering': ['-created_at'],
            },
            bases=('notifications.notification',),
        ),
    ]
