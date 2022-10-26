from django.shortcuts import render
import requests
from django.http import HttpResponse, HttpResponseRedirect
from constants import RECAPTCHA_SECRET_KEY_V2, RECAPTCHA_SECRET_KEY_V3, \
    RECAPTCHA_SITE_KEY_V2, RECAPTCHA_SITE_KEY_V3, MIN_SCORE
from .models import Employee, Event
from django.contrib import messages

def main(request):
       # print(RECAPTCHA_SITE_KEY)
    return render(request, 'main/main.html', {'key': RECAPTCHA_SITE_KEY_V3})


def list(request):
    user_objects = Employee.objects.all()
    print(f'user_objects(list) - {user_objects}')
    #return HttpResponse('user_objects')
    return render(request, 'main/list.html', {'user_objects': user_objects})


def event(request, user_id):
    user_objects = Employee.objects.raw('SELECT * FROM main_employee WHERE id = %s', [user_id])
    events = Event.objects.raw('SELECT * FROM main_event WHERE employee_id = %s', [user_id])
    if request.method == "POST" and request.POST['token']:
        responseCaptcha = requests.post('https://www.google.com/recaptcha/api/siteverify', 
            data={'secret': RECAPTCHA_SECRET_KEY_V3, 'response': request.POST['token']}).json()
        if responseCaptcha['score'] > MIN_SCORE:
            messages.info(request, f"Done - {responseCaptcha['score']}")
            event = request.POST['event']
            employee = Employee.objects.get(id = user_id)
            new_event = Event(employee = employee, message = event)
            if event:
                new_event.save()
        else:
            messages.info(request, f"Not Done - {responseCaptcha['score']}")
    return render(request, 'main/event.html', {'user_objects': user_objects, 'events': events, 'key': RECAPTCHA_SITE_KEY_V3})


def register(request):
    token = request.POST["id_token"]
    responseCaptcha = requests.post('https://www.google.com/recaptcha/api/siteverify', 
        data={'secret': RECAPTCHA_SECRET_KEY_V3, 'response': token}).json()
    print(f'responseCaptcha_v3 - {responseCaptcha} ')
    score = responseCaptcha['score']
    print(score, MIN_SCORE)
    if score < MIN_SCORE:
        messages.info(request, f'NOT Done - {score}')
        return HttpResponseRedirect('/main/recaptcha_v2')
    
    username = request.POST['username']
    password = request.POST['password']
    status  = request.POST['status']
    print(f"username - {username}\npassword - {password}\nstatus - {status}")

    #create data in db
    user = Employee(name = username, mail = password, status = status)
    #user.save()

    messages.info(request, 'Done')
    #return HttpResponse('user_objects')
    return HttpResponseRedirect('/')

def recaptcha_v2(request):
    if request.method == 'GET':
        return render(request, 'main/recaptcha_v2.html', {'key': RECAPTCHA_SITE_KEY_V2})
    elif request.method == "POST":
        token = request.POST['g-recaptcha-response']
        responseCaptcha = requests.post('https://www.google.com/recaptcha/api/siteverify', 
            data={'secret': RECAPTCHA_SECRET_KEY_V2, 'response': token}).json()
        print(f"responseCaptcha_v2 - {responseCaptcha}")
        if responseCaptcha['success'] == True:
            messages.info(request, responseCaptcha['success'])
        else:
            messages.info(request, 'False')
        
        return HttpResponseRedirect('/')
