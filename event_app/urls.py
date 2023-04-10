from django.urls import path
from event_app.views import *


urlpatterns = [
    path('', events, name="home"),
    path('event', events, name="event"),
    path('event/<str:eid>', getEvent, name="get-event"),
    path('register-event/<str:eid>', registerEvent, name="register-event"),
    path('event-register-success', registerEventSuccess, name="event-register-success"),
]

