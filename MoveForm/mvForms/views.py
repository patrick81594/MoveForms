from django.shortcuts import render

from django.http import HttpResponse
from django import template
from django.template import loader
from .models import moveForm


def index(request):
    latest_moveForm_list = moveForm.objects.order_by('-publication_date')[:5]
    template = loader.get_template('mvForms/index.html')
    context = {
            'latest_moveForm_list' : latest_moveForm_list,
        }
    #output = ', '.join([q.fName for q in latest_moveForm_list])
    return render(request, 'mvForms/templates/app/index.html', context)

def details(request, moveForm_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % moveForm_id)


