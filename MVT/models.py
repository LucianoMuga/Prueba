from django.db import models

class Animal(models.Model):
    nombre = models.CharField(max_length = 100)
    raza = models.CharField(max_length = 200)
    edad = models.IntegerField()

    def __str__(self):
        return f"{self.nombre}, {self.edad}, {self.id}"
 

# Create your models here.
