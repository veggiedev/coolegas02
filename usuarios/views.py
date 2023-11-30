from django.shortcuts import render
from .forms import  UserCreation
from django.contrib.auth import logout, authenticate
from django.contrib import messages
from django.contrib.auth.admin import User
from .models import Usuario

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
    return render(request, "perfil.html", context)


def mi_pagina(request):
    user = request.user
    user_info = Usuario.objects.filter(user=user.id).values()
    return render(request, "mi_pagina.html", {"user_info":user_info})
