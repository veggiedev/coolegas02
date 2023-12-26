from django.shortcuts import render
from .models import Actividades, Friendship
from .forms import ActividadesForm, FriendshipForm
from django.views.generic import TemplateView

# Create your views here.

class HomePageView(TemplateView):
    template_name = 'index.html'

def base(request):
    return render(request, "base.html")

def actividades(request):
    lista_actividades = Actividades.objects.all()
    context = {"lista_actividades": lista_actividades,}

    return render(request, "actividades.html", context)

def perfil(request):
    form = ActividadesForm()
    friend_form = FriendshipForm()
    user = request.user
    lista_actividades = Actividades.objects.filter(participantes__email=user.email)
    if request.method == "POST":
        if "create_activity" in request.POST:
            form = ActividadesForm(request.POST)
            if form.is_valid():
                form.save()
        elif "make_friend" in request.POST:
            friend_form = FriendshipForm(request.POST)
            if friend_form.is_valid():
                friend_form.save()
            else:
                print("ERROR : Form is invalid")
    else:
        lista_actividades = Actividades.objects.filter(participantes__email=user.email)
    return render(request, 'perfil.html', {"form" : form, "friend_form": friend_form, "lista_actividades": lista_actividades})

def edit_act(request, id):
    if request.user.is_authenticated:
        actividad = Actividades.objects.get(id=id)
        if request.method == "POST":
            form = ActividadesForm(request.POST, instance=actividad)
            if form.is_valid():
                form.save()
                user = request.user
                lista_actividades = Actividades.objects.filter(participantes__email=user.email)
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
        else:
            friend_form = FriendshipForm()
        return render(request, 'amistades.html', {"friend_form" : friend_form,})

