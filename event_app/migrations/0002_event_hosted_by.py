# Generated by Django 4.0.10 on 2023-04-10 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='hosted_by',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
