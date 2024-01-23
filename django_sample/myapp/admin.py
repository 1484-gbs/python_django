from django.contrib import admin

# Register your models here.

from .models import Employee
from django.contrib.sessions.models import Session

admin.site.register(Employee)
admin.site.register(Session)
