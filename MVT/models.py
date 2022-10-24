from unittest.util import _MAX_LENGTH
from django.db import models

class Animal(models.Model):
    nombre = models.CharField(max_length = 100)
    raza = models.CharField(max_length = 200)
    edad = models.IntegerField()

    def __str__(self):
        return f"{self.nombre}, {self.edad}, {self.id}"
    
class Empleado(models.Model):
    nombre = models.CharField(max_length = 20)
    area = models.CharField(max_length = 30)
    años_de_antiguedad = models.IntegerField()
    
    def __str__(self):
        return f"{self.nombre}, {self.area}, {self.años_de_antiguedad}, {self.id}"
 

# Create your models here.
