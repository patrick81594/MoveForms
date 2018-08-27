from django.contrib import admin
from .models import moveForm, user
from .forms import mvForm
# Register your models here.
admin.site.register(moveForm)
#admin.site.register(user)
class userAdmin(admin.ModelAdmin):
    pass

admin.site.register(user, userAdmin)