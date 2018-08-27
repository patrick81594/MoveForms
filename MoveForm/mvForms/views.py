from .forms import *
from django.forms import modelformset_factory
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django import template
from django.template import loader
from .models import *



def index(request):
    latest_moveForm_list = moveForm.objects.order_by('-publication_date')[:5]
    context = {
            'latest_moveForm_list' : latest_moveForm_list,
        }
    #output = ', '.join([q.fName for q in latest_moveForm_list])
    return render(request, 'index.html', context)


def detail(request, moveForm_id):
    mvFormDetails = get_object_or_404(moveForm, pk = moveForm_id)
    print(mvFormDetails)
    return render(request, 'detail.html', {'MoveForm': mvFormDetails})
    
def form(request):
    if request.method == 'POST':
        form = mvForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
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
            form.save()
        return render(request, 'index.html', context)
    else:
        form = userRegisterForm()

    return render(request, 'userRegister.html', {'form': userRegisterForm()})


