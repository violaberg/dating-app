from django.shortcuts import render

def home(request):
    return render(request, "home/home.html")  # Render the home template


def team(request):
    return render(request, "home/team.html")
