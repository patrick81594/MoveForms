from .forms import *

from django.forms import modelformset_factory
from django.shortcuts import render, get_object_or_404,get_list_or_404
from django.http import HttpResponse
from django import template
from django.template import loader
from .models import *
from django.utils import timezone
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as auth_login
from django.views.generic.list import ListView

def index(request):
    
    latest_moveForm_list = moveForm.objects.order_by('-publication_date')[:5]
    context = {
            'latest_moveForm_list' : latest_moveForm_list,
        }
    #output = ', '.join([q.fName for q in latest_moveForm_list])
    return render(request, 'index.html', context)

def detail(request, moveForm_id):
    mvFormDetails = get_object_or_404(moveForm, pk = moveForm_id)
    
    tasks = list(assignedTask.objects.filter( pk = moveForm_id))
    context = {
        'mvFormDetails' : mvFormDetails,
        'tasks': tasks,
        }
    return render(request, 'detail.html',context)
    
def form(request):
    if request.method == 'POST':
        form = mvForm(request.POST, request.FILES)
        if form.is_valid():
            form_instance = form.save(commit = False)
            form_instance.publication_date = timezone.now()
            form_instance.save()
            latest_moveForm_list = moveForm.objects.order_by('-publication_date')[:5]
            context = {
                 'latest_moveForm_list' : latest_moveForm_list,
            }
            return render(request, 'index.html', context)

    else:
        form = mvForm()
    return render(request, 'form.html', {'form': mvForm()})

def userForm(request):
    latest_moveForm_list = moveForm.objects.order_by('-publication_date')[:5]
    context = {
            'latest_moveForm_list' : latest_moveForm_list,
        }
    if request.method == 'POST':
        form = userRegisterForm(request.POST, request.FILES)
        if form.is_valid():
            user = User.objects.create_user(username=form.cleaned_data['username'], email=form.cleaned_data['eMail'],password=form.cleaned_data['password'])
            user.first_name = form.cleaned_data['firstName']
            user.last_name = form.cleaned_data['lastName']
            
            user.save()
        return render(request, 'index.html', context)
    else:
        form = userRegisterForm()

    return render(request, 'userRegister.html', {'form': userRegisterForm()})

def tasksForm(request, moveForm_id):
    latest_task_list = list(assignedTask.objects.filter(pk = moveForm_id))
    context = {
            'latest_task_list' : latest_task_list,
    }
    if request.method == 'POST':
        form = assignedTaskForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return render(request, 'index.html', context)
    else:
        form = assignedTaskForm()

    return render(request, 'tasks.html', {'form': assignedTaskForm()})


