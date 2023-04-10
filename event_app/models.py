from django.db import models
from accounts.models import *


# Create your models here.



class Event(models.Model):

    name = models.CharField(max_length=250, blank=True, null=True)
    image_url = models.CharField(max_length=250, blank=True, null=True)
    image = models.ImageField(upload_to="event/images/", blank=True, null=True)
    hosted_by = models.CharField(max_length=250, blank=True, null=True)
    location = models.CharField(max_length=250, blank=True, null=True)
    details = models.TextField(max_length=1000, blank=True, null=True)
    fee = models.CharField(max_length=25, default="Free", blank=True, null=True)
    is_paid = models.BooleanField(default=False)
    event_date = models.DateTimeField(blank=True, null=True)
    registration_date = models.DateTimeField(blank=True, null=True)



class EventRegistration(models.Model):

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True, null=True)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, blank=True, null=True)



