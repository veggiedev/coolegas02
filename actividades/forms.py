from django import forms
from .models import Actividades, Friendship
from django.forms.forms import Form
from django.contrib.auth.models import User



class ActividadesForm(forms.ModelForm):

    class Meta:
        model = Actividades

        fields = ("nombre", "participantes", "lugar", "fecha","duracion",)
        widgets = {'fecha':forms.TextInput(attrs={'type':'datetime-local','style': 'width: 80%; display: inline-block; max-width: 600px;'}),
        }
    participantes = forms.ModelMultipleChoiceField(queryset=User.objects.all(),
                                                   label="Participantes",
                                                   widget=forms.CheckboxSelectMultiple)
    nombre = forms.CharField(label='Nombre de Actividad',
                             widget=forms.TextInput(attrs={'placeholder': 'Nombre', 'style': 'width: 80%; display: inline-block; max-width: 600px;', 'class': 'form-control'}))
    lugar = forms.CharField(label='Lugar de Actividad',
                            widget=forms.TextInput(attrs={'placeholder': 'Lugar de Actividad', 'style':'width: 80%; display: inline-block; max-width: 600px;', 'class': 'text'}))
    #fecha = forms.DateField(label='Fecha de Actividad',widget=forms.TextInput(attrs={'placeholder': 'Fecha de Actividad', 'style': 'width: 300px;', 'class': 'form-control'}))
    duracion = forms.IntegerField(label='Duracion de Actividad',widget=forms.TextInput(attrs={'placeholder': 'Duracion de Actividad', 'style':'width: 80%; display: inline-block; max-width: 600px;', 'class': 'form-control'}))

class FriendshipForm(forms.ModelForm):
        #friend_list = User.objects.all()
    #print(friend_list)
    class Meta:
        model = Friendship
        fields = ("friend",)
        #friend = forms.ModelMultipleChoiceField(queryset=User.objects.all(),widget=forms.CheckboxSelectMultiple)
        #friend = forms.MultipleChoiceField(choices=friend_list,
        #                                   label="Amigos",
        #                                   widget=forms.SelectMultiple)
class FriendRequestForm(forms.ModelForm):
    class Meta:
        model = Friendship
        fields = ("friend", "creator_id")
    friend = forms.ModelMultipleChoiceField(queryset=Friendship.objects.all(),
                                           label="Amigos",
                                           widget=forms.CheckboxSelectMultiple)
    creator_id = forms.CharField()
