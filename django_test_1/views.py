from django.shortcuts import render
import requests
from django.http import HttpResponse
from constants import RECAPTCHA_SECRET_KEY_V2, RECAPTCHA_SECRET_KEY_V3, \
    RECAPTCHA_SITE_KEY_V2, RECAPTCHA_SITE_KEY_V3, MIN_SCORE
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'index.html')
    #return HttpResponse('index')