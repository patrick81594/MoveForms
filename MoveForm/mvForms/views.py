from .forms import mvForm
from django.forms import modelformset_factory
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django import template
from django.template import loader
from .models import moveForm



def index(request):
    latest_moveForm_list = moveForm.objects.order_by('-publication_date')[:5]
    context = {
            'latest_moveForm_list' : latest_moveForm_list,
        }
    #output = ', '.join([q.fName for q in latest_moveForm_list])
    return render(request, 'index.html', context)


def detail(request, moveForm_id):
    mvFormDetails = get_object_or_404(moveForm, pk = moveForm_id)
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

