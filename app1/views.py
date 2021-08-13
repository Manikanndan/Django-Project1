from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def app1_first(request):
    return HttpResponse('This is the second app view file.')
