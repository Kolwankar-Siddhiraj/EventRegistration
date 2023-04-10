from datetime import datetime
from django.shortcuts import render, redirect
from event_app.models import *
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.conf import settings
from accounts.access_decorator import *




def sendRegistraionSuccessEmail(user, event):

    domain = "http://127.0.0.1:8000"

    url = f"{domain}/event/{event.id}"

    subject = f"Successfully registered for Event {event.name} !"
    msg = f"Hey {user.first_name} ! \nYou have successfully registered for the event {event.name}."
    html_message = render_to_string('mail_template/event_registration_success.html', {"event_url": url, "event": event})

    res = send_mail(subject, msg, settings.DEFAULT_FROM_EMAIL, [user.email, "siddhirajk77gmail.com"], html_message=html_message, fail_silently=False)
    print("res :: ", res)

    if res == 1:
        return True
    else:
        return False






# Create your views here.

def home(request):

    return render(request, 'home/index.html')


def events(request):

    free = request.GET.get('free', None)
    paid = request.GET.get('paid', None)
    location = request.GET.get('location', None)
    on_date = request.GET.get('on_date', None)
    from_date = request.GET.get('from_date', None)
    to_date = request.GET.get('to_date', None)

    event_filter = {
        "registration_date__gte":datetime.now()
    }

    if free is not None:
        event_filter['is_paid'] = False

    if paid is not None:
        print("paid")
        event_filter['is_paid'] = True
    
    if on_date is not None:
        event_filter['event_date'] = datetime.strptime(on_date, "%d-%m-%Y").date()

    if from_date is not None and to_date is not None:
        event_filter['event_date__range'] = [from_date, to_date]

    if location is not None:
        event_filter['location__icontains'] = location

    event_data = Event.objects.filter(**event_filter)

    print("event_data_length :: ", len(event_data))
    print("event_data :: ", event_data)

    data = {
        "event_data": event_data
    }

    return render(request, 'home/index.html', data)


def getEvent(request, eid):

    event_data = Event.objects.filter(id=eid).first()
    
    data = {
        "event": event_data
    }

    return render(request, 'event/event.html', data)


@authenticated_user
def registerEvent(request, eid):

    print("User :: ", request.user)
    e = Event.objects.filter(id=eid).first()
    user = CustomUser.objects.filter(email=request.user.email).first()
    EventRegistration.objects.create(user=user, event=e)
    
    if sendRegistraionSuccessEmail(request.user, e):
        return redirect('/event-register-success')

    return redirect('/')


@authenticated_user
def registerEventSuccess(request):

        return render(request, 'event/success.html')

