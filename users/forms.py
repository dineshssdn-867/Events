from django.contrib.auth.forms import UserCreationForm  # importing the auth form from django
from .models import CustomUser  # importing user model
from django import forms  # importing form elements


class RegisterForm(UserCreationForm):
    CHOICES = [
        ('is_club_member', 'Club User'),
        ('is_user', 'Normal User')
    ]
    user_types = forms.CharField(label="User Type", widget=forms.RadioSelect(choices=CHOICES))

    username = forms.CharField(max_length=50)  # initializing username field as text
    email = forms.EmailField(max_length=50)     # initializing e-mail field as text
    password1 = forms.CharField()    # initializing password1 field as text
    password2 = forms.CharField()   # initializing password2 field as text
   

    class Meta(UserCreationForm):
        model = CustomUser  # defining the model for using the forms
        fields = ('username', 'email', 'password1', 'password2', 'is_club_member', 'is_user')  # instantiating the forms field
