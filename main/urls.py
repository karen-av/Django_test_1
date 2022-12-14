from django.urls import path
from . import views

app_name = 'main'
urlpatterns = [
    path('',  views.main, name = 'main'),
    path('register',  views.register, name = 'register'),
    path('recaptcha_v2', views.recaptcha_v2, name = 'recaptcha_v2'),
    path('list/', views.list, name = 'list'),
    path('<int:user_id>/event', views.event, name = 'event'),
    path('<int:user_id>/delete', views.delete, name = 'delete')
]

