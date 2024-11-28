from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    return HttpResponse('hello is home page using def function base ')