from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
# Create your views here.

def home(request):
      return HttpResponse('this is home page')

def api_test(request):
      if request.method == 'GET':
            name = request.GET.get('name').strip() 
            email = request.GET.get('email').strip()
            if email == "":
                  email = "not provided"
            contact = request.GET.get('contact').strip()
            message = request.GET.get('message').strip()
            to_mail = request.GET.get('to_mail').strip()
           


            send_mail(
                  f'{name} messaged through your Website...', #subject

                  f'Name: {name}, Email: {email}, Contact: {contact}, Message:{message}', #message
                  'yourcollegeportal@gmail.com', #email_host mail
                  [f'{to_mail}'],
                  fail_silently=False,
                  )          
            return HttpResponse('Message Sent!')
      

