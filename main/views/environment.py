from django.shortcuts import render
from django.contrib import messages
from django.http import Http404

from main.models import Environment

def environmentlist(request):
    environments = Environment.objects.all()
    context={}
    context['environments'] = environments
    messages.info(request, ('所有环境'))
    return render(request, 'environment/environment.html', context)
