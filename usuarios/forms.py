from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.forms.fields import EmailField
from django.forms.forms import Form




class UserCreation(UserCreationForm):
    username = forms.CharField(label='Nombre de usuario', min_length=2, max_length=150,widget=forms.TextInput(attrs={'placeholder': 'Nombre de usuario', 'style': 'width: 80%; display: inline-block; max-width: 600px;', 'class': 'form-control'}))
    email = forms.EmailField(label='Correo Electrónico', widget=forms.EmailInput(attrs={'placeholder' :'Email', 'style': 'width: 80%; display: inline-block; max-width: 600px;'}))
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput(attrs={'placeholder': 'Contrasena', 'style': ',width: 80%; display: inline-block; max-width: 600px;', 'class': 'form-control'}))
    password2 = forms.CharField(label='Confirme Contraseña', widget=forms.PasswordInput(attrs={'placeholder': 'Confirme Contrasena', 'style': 'width: 80%; display: inline-block; max-width: 600px;', 'class': 'form-control'}))
    first_name = forms.CharField(label='Nombre', min_length=5, max_length=150,widget=forms.TextInput(attrs={'placeholder': 'Nombre', 'style': 'width: 80%; display: inline-block; max-width: 600px;', 'class': 'form-control'}))
    last_name = forms.CharField(label='Apellidos', min_length=5, max_length=150,widget=forms.TextInput(attrs={'placeholder': 'Apellidos', 'style': 'width: 80%; display: inline-block; max-width: 600px;', 'class': 'form-control'}))
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )


