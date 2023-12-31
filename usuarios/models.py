from django.db import models
from django.contrib.auth.admin import User
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

# Create your models here.
class Usuario(models.Model):
    user = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)
    edad = models.IntegerField(null=True, blank=True)
    SELECCION_GENERO = (
            ('Hombre', 'Hombre'),
            ('Mujer', 'Mujer'),
            ('Otro', 'Otro'),
            )
    genero = models.CharField(
        max_length=9,
        choices=SELECCION_GENERO,
        default='HOMBRE',
        null=True, blank=True)
   # profile_picture = models.CharField(max_length=350, null=True, blank=True)
   # mis_actividades = models.ManyToManyField(Actividades)
    def __str__(self):
        return self.user.first_name + " " +  self.user.last_name

class Friends(models.Model):
    users = models.ManyToManyField(Usuario)
    current_user=models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='owner')

    @classmethod
    def make_friend(cls, current_user, new_friend):
        friend, created = cls.objects.get_or_create(
            current_user = current_user
        )
        friend.users.add(new_friend)

    @classmethod
    def remove_friend(cls, current_user, new_friend):
        friend, created = cls.objects.get_or_create(
            current_user = current_user
        )
        friend.users.remove(new_friend)

    def __str__(self):
        return str(self.current_user)

@login_required
def add_or_remove_friends(request, username, verb):
    n_f = get_object_or_404(User, username=username)
    owner = request.user.userprofile
    new_friend = UserProfile.objects.get(user=n_f)

    if verb == "add":
        new_friend.followers.add(owner)
        Friend.make_friend(owner, new_friend)
    else:
        new_friend.followers.remove(owner)
        Friend.remove_friend(owner, new_friend)

    return redirect(new_friend.get_absolute_url())
