from django import forms
from .models import Actividades, Friendship
from django.forms.forms import Form
from usuarios.models import CustomUser



class ActividadesForm(forms.ModelForm):

    class Meta:
        model = Actividades

        fields = ("nombre", "participantes", "lugar", "fecha","duracion",)
        widgets = {'fecha':forms.TextInput(attrs={'type':'datetime-local','style': 'width: 80%; display: inline-block; max-width: 600px;'}),
        }
    participantes = forms.ModelMultipleChoiceField(queryset=CustomUser.objects.all(),
                                                   label="Participantes",
                                                   widget=forms.CheckboxSelectMultiple)
    nombre = forms.CharField(label='Nombre de Actividad', widget=forms.TextInput(attrs={'placeholder': 'Nombre', 'style': 'width: 80%; display: inline-block; max-width: 600px;', 'class': 'form-control'}))
    lugar = forms.CharField(label='Lugar de Actividad', widget=forms.TextInput(attrs={'placeholder': 'Lugar de Actividad', 'style':'width: 80%; display: inline-block; max-width: 600px;', 'class': 'text'}))
    #fecha = forms.DateField(label='Fecha de Actividad',widget=forms.TextInput(attrs={'placeholder': 'Fecha de Actividad', 'style': 'width: 300px;', 'class': 'form-control'}))
    duracion = forms.IntegerField(label='Duracion de Actividad', widget=forms.TextInput(attrs={'placeholder': 'Duracion de Actividad', 'style':'width: 80%; display: inline-block; max-width: 600px;', 'class': 'form-control'}))

class FriendshipForm(forms.ModelForm):
    class Meta:
        model = Friendship
        fields = ("friends", "creator_id")
    friends = forms.ModelMultipleChoiceField(queryset=CustomUser.objects.all(),
                                           label="Amigos",
                                           widget=forms.CheckboxSelectMultiple)
    creator_id = forms.CharField()

