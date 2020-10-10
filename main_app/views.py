from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
      return HttpResponse('this is home page')

def api_test(request):
      return HttpResponse('response of api')