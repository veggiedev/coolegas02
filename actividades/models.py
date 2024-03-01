from django.contrib.auth.admin import User
from django.db import models


# Create your models here.
class Actividades(models.Model):
    nombre = models.CharField(max_length=150)
    lugar = models.CharField(max_length=300)
    fecha = models.DateTimeField()
    duracion = models.IntegerField()
    participantes = models.ManyToManyField(User)

    def __str__(self):
        return self.nombre


class Friendship(models.Model):
    friend = models.ForeignKey(User, blank=True, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    creator_id = models.ForeignKey(
        User, related_name="Creador", on_delete=models.CASCADE
    )

    def recibidas(self):
        list = []
        for i in Friendship.objects.filter(friend__username == self.user__username):
            list.append(i)
        return list

    def enviadas(self):
        pass

    def reciprocas(self):
        pass

    def __str__(self):
        return f"{self.creator_id.username.capitalize()} added {self.friend.username.capitalize()}"
