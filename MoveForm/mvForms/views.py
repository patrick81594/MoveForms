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
    moveFmFormSet = modelformset_factory(moveForm, fields = ('fName', 'lName', 'eMail', 'Citizenship','Company',
                  'Manager', 'subPOC', 'program', 'location', 'phoneNum', 'faaBadge', 'faaParking', 'comments'))
    if request.method == 'POST':
        formset = moveFmFormSet(request.POST, request.FILES, instance = moveForm)
        if formset.is_valid():
            formset.save()
            latest_moveForm_list = moveForm.objects.order_by('-publication_date')[:5]
            context = {
                 'latest_moveForm_list' : latest_moveForm_list,
            }
            render(request, 'index.html', context)

    else:
        formset = moveFmFormSet()
    return render(request, 'form.html', {'form': mvForm()})

