from django.urls import path, include
from actividades import views

urlpatterns = [
    path("", views.HomePageView.as_view(), name="index"),
    path("actividades", views.actividades, name="actividades"),
    path("base", views.base, name="base"),
    path("perfil", views.perfil, name="perfil"),
    path("edit_act/<int:id>", views.edit_act, name="edit_act"),
]

