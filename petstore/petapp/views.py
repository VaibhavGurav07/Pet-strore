from django.shortcuts import render, HttpResponse
from django.views import View

# Create your views here.

def home(request):
    return HttpResponse('hello is home page using def function base ')

class MyView(View):

    def get(self,request):

        return HttpResponse('hello from class base view ')
