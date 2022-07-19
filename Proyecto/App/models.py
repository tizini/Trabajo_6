from django.db import models

# Create your models here.

class Familia(models.Model):
    tipo = models.CharField(max_length=50)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)    
    edad = models.IntegerField()
    
