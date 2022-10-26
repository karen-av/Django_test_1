from django.contrib import admin

# Register your models here.
from .models import Employee, Event

admin.site.register(Employee)
admin.site.register(Event)