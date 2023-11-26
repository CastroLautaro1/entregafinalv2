from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Articulo(models.Model):
    titulo = models.CharField(max_length=64)
    subtitulo = models.CharField(max_length=32)
    cuerpo = models.CharField(max_length=1200)
    autor = models.CharField(max_length=32)
    fecha = models.IntegerField()
    
class Compacto(models.Model):
    marca = models.CharField(max_length=32)
    modelo = models.CharField(max_length=32)
    anio = models.IntegerField()
    
    def __str__(self):
        return f"{self.modelo} ({self.anio})"
    
class SUV(models.Model):
    marca = models.CharField(max_length=32)
    modelo = models.CharField(max_length=32)
    anio = models.IntegerField()
    
    def __str__(self):
        return f"{self.modelo} ({self.anio})"
    
class Sedan(models.Model):
    marca = models.CharField(max_length=32)
    modelo = models.CharField(max_length=32)
    anio = models.IntegerField()
    
    def __str__(self):
        return f"{self.modelo} ({self.anio})"

class PickUp(models.Model):
    marca = models.CharField(max_length=32)
    modelo = models.CharField(max_length=32)
    anio = models.IntegerField()
    
    def __str__(self):
        return f"{self.modelo} ({self.anio})"
    
