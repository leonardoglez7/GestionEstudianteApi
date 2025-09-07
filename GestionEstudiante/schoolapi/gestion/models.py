from django.db import models

# Create your models here.

class Asignatura(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class student(models.Model):
    nombre = models.CharField(max_length=100)
    email =  models.EmailField(unique=True)
    asignaturas = models.ManyToManyField(Asignatura)

    def __str__(self):
        return self.nombre

