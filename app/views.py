from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def hai(request):
    return HttpResponse('This is my first app file.')

def hello(request):
    return HttpResponse('<h1><marquee>This is my second app file.</marquee></h1>')