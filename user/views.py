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
# def home(request):
#     users = User.objects.all()
#     form = NewUserForm()
#     return render(request, 'home.html', {'form': form, 'users':users})

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
    form = EditUserForm(instance=user)
    print(form, "yes 1")
    if request.method == 'POST':
        form = EditUserForm(request.POST)
        if form.is_valid():
            print(form, "yes")
            # first_name = form.cleaned_data['first_name']
            # middle_initial = form.cleaned_data['middle_initial']
            # last_name = form.cleaned_data['last_name']
            # suffix = form.cleaned_data['suffix']
            # full_name = form.cleaned_data['full_name']
            # email = form.cleaned_data['email']
            # gender = form.cleaned_data['gender']

            form.cleaned_data
            form.save()

    return render(request, 'user.html', {'form': form, 'user':user})

# saves new user data
def post(request):
    users = User.objects.all()
    form = NewUserForm()

    
    if request.method == 'POST':
        form = NewUserForm(request.POST)

        print(form)
        if form.is_valid():
            print(form)

            form.save()

            form = NewUserForm()
        
            
            


    return render(request, 'home.html', {'form': form, 'users':users})


