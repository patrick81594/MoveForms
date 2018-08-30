from django.contrib import admin
from .models import moveForm, user, assignedTask
from .forms import mvForm
from . import models
from django.contrib.auth.models import User
## Register your models here.

class inline(admin.TabularInline):
    model = models.assignedTask
    extra = 0

@admin.register(moveForm)
class moveFormAdmin(admin.ModelAdmin):
    list_display = ("First_Name", "Last_Name", "_tasks")
    list_display_links = ("First_Name", "_tasks")
    search_fields = ["User__username"] 
    inlines = [
        inline
    ]
    def _tasks(self, obj):
        tasks = assignedTask.objects.filter(pk = obj.pk)
        return tasks.all().count()
