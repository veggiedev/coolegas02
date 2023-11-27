from django.urls import path, include

from actividades import views

urlpatterns = [
    path("", views.index, name="index"),
    path("actividades", views.actividades, name="actividades"),
    path("base", views.base, name="base"),
    path("accounts/", include("django.contrib.auth.urls")),
    path("mis_actividades", views.mis_actividades, name="mis_actividades"),
    path("edit_act/<int:id>", views.edit_act, name="edit_act"),
]

