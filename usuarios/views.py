from django.shortcuts import render
from .forms import  CustomUserCreationForm
from django.contrib.auth import logout, authenticate
from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import LoginForm
from django.contrib.auth import views as auth_views

from django.contrib.auth import logout

# Create your views here.
class registro(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registro.html" 
    # if request.method == 'POST':
    #     form = CustomUserCreationForm(request.POST)
    #     if form.is_valid():
    #         # username = form.cleaned_data.get('username')
    #         raw_password = form.cleaned_data.get('password1')
    #         #user = authenticate(username=username, password=raw_password)
    #         form.save()
    #         messages.success(request, 'Cuenta creada!')
    #         return redirect('login') 
    #     else:
    #         print("Form Invalid!!!")
    # else:
    #     form = CustomUserCreationForm()
    # context = {
    #         'form':form,
    #         }
    # return render(request, "registro.html", context)
    #

# def mi_pagina(request):
#     user = request.user
#     user_info = CustomUser.objects.filter(user=user.id).values()
#     return render(request, "mi_pagina.html", {"user_info":user_info})
class LoginView(auth_views.LoginView):
    form_class = LoginForm
    template_name = 'registration/login.html'


def logout_view(request):
    logout(request)
