from django.shortcuts import render
from .models import *

def home(request):
    context = {
        "profile": Profile.objects.first(),
        "skills": Skill.objects.all(),
        "projects": Project.objects.all(),
        "services": Service.objects.all(),
        "testimonials": Testimonial.objects.all(),
        "settings": SiteSettings.objects.first(),
    }
    return render(request, "kenya/index.html", context)

def about(request):
    return render(request, "kenya/about.html")

def projects(request):
    return render(request, "kenya/projects.html")

def blog(request):
    return render(request, "kenya/blog.html")

def contact(request):
    return render(request, "kenya/contact.html")