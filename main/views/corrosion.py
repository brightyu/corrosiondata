from django.shortcuts import render
from django.contrib import messages
from django.http import Http404

from main.models import CorrosionResult

def corrosionlist(request):
    rates = CorrosionResult.objects.all()
    context={}
    context['rates']=rates
    messages.info(request, ('所有腐蚀速率'))
    return render(request, 'corrosionresult/corrosion.html', context)
