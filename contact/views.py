from django.shortcuts import render
from django.http import JsonResponse
from .utils import send_email
from .forms import ContactForm


from django.shortcuts import render, redirect
from .forms import ContactForm
from .utils import send_email

def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            
            response = send_email(email, subject, message)
            
            if "id" in response:
                return redirect('contact_success')
            else:
                form.add_error(None, "There was an error sending your message. Please try again.")
    else:
        form = ContactForm()

    return render(request, 'contact/contact.html', {'form': form})


def contact_success(request):
    return render(request, 'contact/contact_success.html')
