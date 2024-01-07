from django import forms
from .models import Actividades, Friendship
from django.forms.forms import Form
from django.contrib.auth.models import User



class ActividadesForm(forms.ModelForm):

    class Meta:
        model = Actividades

        fields = ("nombre", "participantes", "lugar", "fecha","duracion",)
        widgets = {'fecha':forms.TextInput(attrs={'type':'datetime-local','style': ' border-bottom: solid 1px rgb(21 128 61);display: inline-block;'}),
        }
    participantes = forms.ModelMultipleChoiceField(queryset=User.objects.all(), label="Participantes",widget=forms.CheckboxSelectMultiple)
    nombre = forms.CharField(label='Nombre de Actividad',
                             widget=forms.TextInput(attrs={'placeholder': 'Nombre', 'style':'border-bottom: solid 1px rgb(21 128 61);', 'class': 'form-control'}))
    lugar = forms.CharField(label='Lugar de Actividad', widget=forms.TextInput(attrs={'placeholder': 'Lugar de Actividad', 'style':'border-style: solid; border-bottom: solid 1px rgb(21 128 61);', 'class': 'text'}))
    #fecha = forms.DateField(label='Fecha de Actividad',widget=forms.TextInput(attrs={'placeholder': 'Fecha de Actividad', 'style': 'width: 300px;', 'class': 'form-control'}))
    duracion = forms.IntegerField(label='Duracion de Actividad',widget=forms.TextInput(attrs={'placeholder': 'Duracion de Actividad', 'style':'border-bottom: solid 1px rgb(21 128 61);', 'class': 'form-control'}))

class FriendshipForm(forms.ModelForm):
    class Meta:
        model = Friendship
        fields = ("friends", "creator_id",)
    friends = forms.ModelMultipleChoiceField(queryset=User.objects.all(),
                                           label="Amigos",
                                           widget=forms.CheckboxSelectMultiple)
    creator_id = forms.CharField()

