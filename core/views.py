from django.shortcuts import render
from .models import Service

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def services(request):
    services_list = Service.objects.all()
    return render(request, 'services.html', {'services': services_list})

def contact(request):
    return render(request, 'contact.html')