from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# request -> response
# request handler
# action 
# Django template = React views

def say_hello(request):
    # return HttpResponse('Hello World')
    return render(request, 'user.html', {'name': 'Mosh'})