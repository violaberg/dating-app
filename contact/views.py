from django.shortcuts import render


def contact(request):
    return render(request, 'contact/contact.html')


def contact_success(request):
    return render(request, 'contact/contact_success.html')
