from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Service, CoreValue, TeamMember, Testimonial, FAQ, Partner, BlogPost, Subscriber, HeroSlide

def home(request):
    partners = Partner.objects.all()
    latest_posts = BlogPost.objects.all()[:3]
    slides = HeroSlide.objects.all()
    return render(request, 'home.html', {
        'partners': partners, 
        'latest_posts': latest_posts,
        'slides': slides
    })
# (Acha views zingine zilizobaki kama zilivyo)

def about(request):
    context = {
        'values': CoreValue.objects.all(),
        'team': TeamMember.objects.all(),
        'testimonials': Testimonial.objects.all(),
    }
    return render(request, 'about.html', context)

def services(request):
    return render(request, 'services.html', {'services': Service.objects.all()})

def faq(request):
    return render(request, 'faq.html', {'faqs': FAQ.objects.all()})

def contact(request):
    return render(request, 'contact.html')

def blog_list(request):
    posts = BlogPost.objects.all()
    return render(request, 'blog.html', {'posts': posts})

def blog_detail(request, slug):
    post = get_object_or_404(BlogPost, slug=slug)
    return render(request, 'blog_detail.html', {'post': post})

def subscribe(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        if email:
            if Subscriber.objects.filter(email=email).exists():
                messages.info(request, 'You are already subscribed!')
            else:
                Subscriber.objects.create(email=email)
                messages.success(request, 'Thank you for subscribing!')
    return redirect(request.META.get('HTTP_REFERER', '/'))