from django.shortcuts import render
from django.contrib import messages
from django.http import Http404

from main.models import Chemical

def chemicallist(request):
    materials = Chemical.objects.all()
    context={}
    context['materials']=materials
    messages.info(request, ('所有材料'))
    return render(request, 'chemical/chemical.html', context)
