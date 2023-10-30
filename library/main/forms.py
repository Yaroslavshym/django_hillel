from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User

class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Login', widget=forms.TextInput(attrs={'class': 'from-control'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'password'}))

class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Login', widget=forms.TextInput(attrs={'class': 'from-control'}))
    email = forms.CharField(label='Email', widget=forms.EmailInput(attrs={'class': 'from-control'}))
    first_name = forms.CharField(label='first_name', widget=forms.TextInput(attrs={'class': 'from-control'}))
    last_name = forms.CharField(label='last_name', widget=forms.TextInput(attrs={'class': 'from-control'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'from-control'}))
    password2 = forms.CharField(label='Password confirm', widget=forms.PasswordInput(attrs={'class': 'from-control'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'first_name', 'last_name')
        
