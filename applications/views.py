from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegistrationForm

def home(request):
    return render(request, 'home.html')


def register(request):
    registration_form = RegistrationForm()
    return render(request, 'register.html', {'registration_form': registration_form})