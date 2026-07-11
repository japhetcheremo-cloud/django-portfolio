from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("projects/", views.projects, name="projects"),
    path("blog/", views.blog, name="blog"),
    path("contact/", views.contact, name="contact"),

    # M-Pesa
    path("pay/", views.pay_mpesa, name="pay"),
    path("mpesa/callback/", views.mpesa_callback, name="callback"),
]