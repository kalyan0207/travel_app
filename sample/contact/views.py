

# Create your views here.
from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'nxt.html')                

        return redirect('/')
    form = ContactForm()
    return render(request, 'contact.html', {'form' : form})