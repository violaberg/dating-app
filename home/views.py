from django.shortcuts import render

def home(request):
    return render(request, "home/home.html")


def team(request):
    return render(request, "home/team.html")


def about(request):
    return render(request, "home/about.html")


def policy(request):
    return render(request, "home/privacy_policy.html")
