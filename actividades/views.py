from django.shortcuts import render
from .models import Actividades, Friendship
from .forms import ActividadesForm, FriendshipForm

# Create your views here.

def index(request):
    return render(request, "index.html")

def base(request):
    return render(request, "base.html")

def actividades(request):
    lista_actividades = Actividades.objects.all()
    context = {"lista_actividades": lista_actividades,}

    return render(request, "actividades.html", context)
def logout(request):
    return render(request, "login.html", {"form":form})

def perfil(request):
    if request.method == "POST":
        form = ActividadesForm(request.POST)
        if form.is_valid():
            form.save()
    form = ActividadesForm()
    user = request.user
    lista_actividades = Actividades.objects.filter(participantes__username=user.username)
    return render(request, 'perfil.html', {"form": form, "lista_actividades": lista_actividades})

def edit_act(request, id):
    if request.user.is_authenticated:
        actividad = Actividades.objects.get(id=id)
        if request.method == "POST":
            form = ActividadesForm(request.POST, instance=actividad)
            if form.is_valid():
                form.save()
                user = request.user
                lista_actividades = Actividades.objects.filter(participantes__username=user.username)
                return render(request, 'mis_actividades.html', {"form": form, "lista_actividades": lista_actividades})

        else:
            form = ActividadesForm(instance=actividad)
        return render(request, 'edit_actividad.html', {'form':form})

def amistades(request):
    if request.user.is_authenticated:
        user = request.user
        if request.method == "POST":
            friend_form = FriendshipForm(request.POST)
            if friend_form.is_valid():
                friend_form.save()
            friend_form = FriendshipForm()
            lista_amigos = Friendship.objects.filter(creator_id__username=user.username)
            return render(request, 'amistades.html', {"friend_form" : friend_form, "lista_amigos" : lista_amigos})

        friend_form = FriendshipForm()
        lista_amigos = Friendship.objects.filter(creator_id__username=user.username)
        return render(request, 'amistades.html', {"friend_form" : friend_form, "lista_amigos" : lista_amigos})

