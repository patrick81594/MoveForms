from django.contrib import admin
from .models import moveForm, user, assignedTask
from .forms import mvForm
from django.contrib.auth.models import User
# Register your models here.
admin.site.register(moveForm)
#admin.site.register(user)
admin.site.register(assignedTask)