# Generated by Django 4.0.10 on 2023-04-10 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event_app', '0003_event_fee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='fee',
            field=models.CharField(blank=True, default='Free', max_length=25, null=True),
        ),
    ]
