
from django.urls import path

from .views import *
from . import views
from django.contrib.auth import views as auth_views
app_name = 'mvForms'
urlpatterns = [
    path('', views.index, name='index'),
    path('tasks/<int:moveForm_id>/', views.tasksForm, name = "tasks"),
    path('<int:moveForm_id>/', views.detail, name = "detail"),
    path('form/', views.form, name = "form"),
    path('regUser/', views.userForm, name = "userRegister"),
    
   
]