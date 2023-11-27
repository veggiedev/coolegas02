from django.urls import path
from.  import views

urlpatterns =[
    path('registro', views.registro, name='registro'),
    path('perfil', views.perfil, name='perfil'),
    path('mi_pagina', views.mi_pagina, name='mi_pagina'),

]
