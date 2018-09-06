from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return HttpResponse('<html><title>Goodlark Educational Foundation</title></html>')