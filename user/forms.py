from django import forms
from .models import User

class NewUserForm(forms.ModelForm):
    class Meta: 
        model = User
        fields = ['first_name', 
                  'middle_initial',
                  'last_name',
                  'suffix',
                  'full_name',
                  'email',
                  'gender'
                  ]