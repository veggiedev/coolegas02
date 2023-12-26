from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.core.exceptions import ValidationError
from usuarios.models import CustomUser
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

User = get_user_model()



SELECCION_GENERO = (
        ('Hombre', 'Hombre'),
        ('Mujer', 'Mujer'),
        ('Otro', 'Otro'),
        )

class CustomUserCreationForm(ModelForm):
    class Meta:
        model = CustomUser
        fields = ("email",)
        
    email = forms.EmailField(label='Correo Electrónico', widget=forms.EmailInput(attrs={'placeholder' :'Email', 'style': 'width: 80%; display: inline-block; max-width: 600px;'}))
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput(attrs={'placeholder': 'Contrasena', 'style': ',width: 80%; display: inline-block; max-width: 600px;', 'class': 'form-control'}))
    password2 = forms.CharField(label='Confirme Contraseña', widget=forms.PasswordInput(attrs={'placeholder': 'Confirme Contrasena', 'style': 'width: 80%; display: inline-block; max-width: 600px;', 'class': 'form-control'}))
    first_name = forms.CharField(label='Nombre', min_length=5, max_length=150,widget=forms.TextInput(attrs={'placeholder': 'Nombre', 'style': 'width: 80%; display: inline-block; max-width: 600px;', 'class': 'form-control'}))
    last_name = forms.CharField(label='Apellidos', min_length=5, max_length=150,widget=forms.TextInput(attrs={'placeholder': 'Apellidos', 'style': 'width: 80%; display: inline-block; max-width: 600px;', 'class': 'form-control'}))
    genero = forms.MultipleChoiceField(
        choices=SELECCION_GENERO)
    edad = forms.IntegerField() 


class CustomUserChangeForm(ModelForm):
    class Meta:
        model = CustomUser
        fields = ("email",)

class LoginForm(AuthenticationForm):
    pass
