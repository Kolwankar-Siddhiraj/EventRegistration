# Generated by Django 4.0.10 on 2023-04-10 18:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event_app', '0004_alter_event_fee'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='image',
        ),
    ]
