from django.db import models
from django.contrib.auth.admin import User
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
    friends = models.ManyToManyField(User, blank=True, null=True)
    created = models.DateTimeField(related_name="Date", auto_now_add=True)
    creator_id = models.ForeignKey(User, relatde_name="Creador", on_delete=models.CASCADE)
