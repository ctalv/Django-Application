from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_http_methods
from django.http import HttpResponse
from .models import User
from .forms import NewUserForm, EditUserForm

# Create your views here.
# request -> response
# request handler
# action 
# Django template = React views


def edit(request, user_id):
    user = User.objects.get(pk=user_id)
    form = EditUserForm(instance=user)
    if request.method == 'POST':
        form = EditUserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            

    return render(request, 'user.html', {'form': form, 'user':user})

# saves new user data
def post(request):
    users = User.objects.all()
    form = NewUserForm()

    
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():

            form.save()

            form = NewUserForm()
        
            

    return render(request, 'home.html', {'form': form, 'users':users})


