from django.db import models
from usuarios.models import CustomUser

# Create your models here.
class Actividades(models.Model):
    nombre = models.CharField(max_length=150)
    lugar = models.CharField(max_length=300)
    fecha = models.DateTimeField()
    duracion = models.IntegerField()
    participantes = models.ManyToManyField(CustomUser)
    def __str__(self):
        return self.nombre

class Friendship(models.Model):
    friends = models.ManyToManyField(CustomUser)
    created = models.DateTimeField(auto_now_add=True)
    creator_id = models.CharField(max_length= 30)
    def __str__(self):
        return self.creator_id

