from django.urls import path
from . import views

app_name = 'main'
urlpatterns = [
    path('',  views.main, name = 'main'),
    path('register',  views.register, name = 'register'),
    path('recaptcha_v2/', views.recaptcha_v2, name = 'recaptcha_v2'),
    path('list/', views.list, name = 'list'),
]

