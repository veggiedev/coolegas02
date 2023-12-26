from django.urls import path, include
from.  import views
from .views import LoginView, registro

urlpatterns =[
    path('registro', registro.as_view(), name='registro'),
    path('accounts/', include('allauth.urls')), # new
    path('logout/', include('allauth.urls')), # new

    path("logout", views.logout_view, name="logout"),
]
