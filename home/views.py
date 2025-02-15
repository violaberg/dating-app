from django.shortcuts import render
from .models import FAQ


def home(request):
    """ A view to return the Home page"""
    return render(request, "home/home.html")


def team(request):
    """ A view to return the Team page"""
    return render(request, "home/team.html")


def about(request):
    """ A view to return the About page"""
    return render(request, "home/about.html")


def policy(request):
    """ A view to return the Privacy Policy page"""
    return render(request, "home/privacy_policy.html")


def faq(request):
    """ A view to return the FAQ page"""
    faqs = FAQ.objects.all()

    return render(request, "home/faq.html", {'faqs': faqs})
