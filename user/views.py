from django.shortcuts import render, get_object_or_404
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
def edit(request, user_id):
    user = User.objects.get(pk=user_id)
    print(user.first_name)
    form = EditUserForm(instance=user)
    if form.is_valid():
        form.save()

    return render(request, 'user.html', {'form': form, 'user':user})

# saves new user data
def post(request):
    users = User.objects.all()
    form = NewUserForm(request.POST)
    # print(form)
    if form.is_valid():
        try:
            form.save()
        # text = form.cleaned_data['post'] # checks security
        # print(text)
            form = NewUserForm()
            return HttpResponse('Saved to database.')
        except Exception as e:
            error_message = str(e)
            return error_message  

    return render(request, 'home.html', {'form': form, 'users':users})


