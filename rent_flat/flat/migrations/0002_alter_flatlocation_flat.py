# Generated by Django 4.2.6 on 2024-03-13 20:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('flat', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flatlocation',
            name='flat',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='location', to='flat.flat'),
        ),
    ]
