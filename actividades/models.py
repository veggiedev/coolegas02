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


