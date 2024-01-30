from django.shortcuts import render
from .models import Actividades, Friendship
from .forms import ActividadesForm, FriendRequestForm, FriendshipForm
from django.contrib.auth.models import User
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

def amistades(request,id):
    if request.user.is_authenticated:
        creator_id = User.objects.get(id=id)
        print(creator_id)
        user = request.user
        amistades_enviadas = Friendship.objects.filter(creator_id__username=user.username)  #OBJETOS AMISTAD CREADOS POR MI
        #print(f"enviadas por mi{[i.friend.username for i in amistades_enviadas]}") #this is okj
        amistades_recibidas = Friendship.objects.filter(friend__username=user.username) #OBJETOS AMISTAD CREADOS POR OTROS PARA MI
        #print(f"recibidas{[i.creator_id.username for i in amistades_recibidas]}") #this is okj
        lista_amistades_reciprocas = []
        lista_amistades_enviadas = []
        lista_amistades_recibidas = []
        for i in amistades_recibidas:
            for j in amistades_enviadas:
                if i.friend.username == j.creator_id.username:
                    if j.friend.username == i.creator_id.username:
                        if i.creator_id.username not in lista_amistades_reciprocas:
                            lista_amistades_reciprocas.append(i.creator_id.username)
                #print(lista_amistades_reciprocas)
        for i in amistades_enviadas:
            for j in amistades_recibidas:
                if i.creator_id.username == j.creator_id.username:
                    if i not in lista_amistades_reciprocas:
                        lista_amistades_reciprocas.append(i.creator_id.username)
                #print(lista_amistades_reciprocas)
        for i in amistades_recibidas:
            if i not in lista_amistades_reciprocas:
                lista_amistades_recibidas.append(i.creator_id.username)
        #print(lista_amistades_recibidas)
        if request.method == "POST":
            friend_form = FriendshipForm(request.POST)
            friend_request_form = FriendRequestForm(request.POST)
            if friend_form.is_valid():
                form = friend_form.save(commit=False)
                form.creator_id = creator_id
                friend_form.save()
            elif friend_request_form.is_valid():
                friend_request_form.save()
        else:
            friend_form = FriendshipForm()
            friend_request_form = FriendRequestForm()
        return render(request, 'amistades.html', {
            "friend_form" : friend_form, "friend_request_form" : friend_request_form,
            "lista_amistades_enviadas":lista_amistades_enviadas,
            "lista_amistades_recibidas":lista_amistades_recibidas,
            "lista_amistades_reciprocas":lista_amistades_reciprocas
            }
        )

