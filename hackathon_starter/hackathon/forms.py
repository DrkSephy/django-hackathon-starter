from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from hackathon.models import UserProfile

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')
