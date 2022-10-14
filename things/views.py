from django.shortcuts import render
from .forms import FormUpForm

def home(request):
    return render(request, 'home.html')

def form_up(request):
    form = FormUpForm()
    return render(request, "home.html", { "form" : form })
