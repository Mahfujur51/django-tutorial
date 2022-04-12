from pyexpat import model
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from session.models import Profile


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email','first_name','last_name' ,'password1', 'password2')

class UserProfileForm(forms.ModelForm):
    birth_date=forms.DateField(widget=forms.TextInput(attrs={'type':'date'}))
    class Meta:
        model=Profile
        exclude=('user',)