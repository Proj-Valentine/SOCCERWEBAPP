from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request, 'index.html', context={})

def profile (request):
    return render(request, 'profile.html', context={})

def schedules (request):
    return render(request, 'schedules.html', context={})

def contacts (request):
    return render(request, 'contact.html', context={})
