from django.shortcuts import render
from .models import Service, CoreValue, TeamMember, Testimonial

def home(request):
    return render(request, 'home.html')

def about(request):
    values = CoreValue.objects.all()
    team = TeamMember.objects.all()
    testimonials = Testimonial.objects.all()
    context = {
        'values': values,
        'team': team,
        'testimonials': testimonials,
    }
    return render(request, 'about.html', context)

def services(request):
    services_list = Service.objects.all()
    return render(request, 'services.html', {'services': services_list})

def contact(request):
    return render(request, 'contact.html')