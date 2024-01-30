from django.shortcuts import render
from .forms import  UserCreation
from django.contrib.auth import logout, authenticate
from django.contrib import messages
from django.contrib.auth.admin import User
from .models import Usuario
from actividades.models import Friendship

# Create your views here.
def registro(request):
    if request.method == 'POST':
        form = UserCreation(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            registro(request)
            messages.success(request, 'Cuenta creada!')
    else:
        form = UserCreation()
    context = {
            'form':form
            }
    return render(request, "registro.html", context)


def mi_pagina(request):
    user = request.user
    user_info = Usuario.objects.filter(user=user.id).values()
    user = request.user                                                                                                          
    amistades_enviadas = Friendship.objects.filter(creator_id__username=user.username)  #OBJETOS AMISTAD CREADOS POR MI     ■ Can
    amistades_recibidas = Friendship.objects.filter(friend__username=user.username) #OBJETOS AMISTAD CREADOS POR OTROS PARA MI   
    lista_amistades_recibidas = []
    print(lista_amistades_recibidas)
    lista_amistades_reciprocas = []
    for i in amistades_recibidas:                                                                                                   
        for j in amistades_enviadas:                                                                                             
            if i.friend.username == j.creator_id.username:
                if j.friend.username == i.creator_id.username:
                    if i.creator_id.username not in lista_amistades_reciprocas:
                        lista_amistades_reciprocas.append(i.creator_id.username)
    for i in amistades_enviadas:
        for j in amistades_recibidas:                                                                                            
            if i.creator_id.username == j.creator_id.username:                                                                   
                if i not in lista_amistades_reciprocas:                                                                          
                    lista_amistades_reciprocas.append(i.creator_id.username)                                                     
                #print(lista_amistades_reciprocas)                                                                                   
    for i in amistades_recibidas:                                                                                                
        if i not in lista_amistades_reciprocas:
            lista_amistades_recibidas.append(i.creator_id.username)
    return render(request, "mi_pagina.html", {"user_info":user_info, "reciprocas":lista_amistades_reciprocas, "recibidas":lista_amistades_recibidas})
