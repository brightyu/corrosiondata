from django.http import HttpResponse
from django.shortcuts import render
from main.models import Chemical

def index(request):
    Chemical_list = Chemical.objects.all()
    return render(request, 'index.html')

