from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import User
from .forms import NewUserForm, EditUserForm

# Create your views here.
# request -> response
# request handler
# action 
# Django template = React views

# display form
def home(request):
    users = User.objects.all()
    form = NewUserForm()
    return render(request, 'home.html', {'form': form, 'users':users})

# populates form with user info to be edited and added to database
# def edit(request, user_id):
#     user = User.objects.get(pk=user_id)
#     print(user.first_name)
#     form = EditUserForm(instance=user)
#     # if request.method == 'POST':
#     #     form = EditUserForm(request.POST)
#     #     if form.is_valid():
#     #         form.save()

#     return render(request, 'user.html', {'form': form, 'user':user})

# populates form with user info to be edited and added to database
def edit(request, user_id):
    user = User.objects.get(pk=user_id)
    print(user.first_name)
    form = EditUserForm(instance=user)
    print(form)
    if request.method == 'POST':
        form = EditUserForm(request.POST)
        if form.is_valid():
            print(form)
            form.save()

    return render(request, 'user.html', {'form': form, 'user':user})

# saves new user data
def post(request):
    users = User.objects.all()
    
    # print(form)
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save()
        # text = form.cleaned_data['post'] # checks security
        # print(text)
            form = NewUserForm()
            return HttpResponse('Saved to database.')


    return render(request, 'home.html', {'form': form, 'users':users})


