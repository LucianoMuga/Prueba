from django.shortcuts import render
from MVT.models import Animal
from django.http import HttpResponse

def index(request):
    return render(request, "MVT/index.html")


def mostrarAnimal(request):
    lista_animales = Animal.objects.all()
    return render(request, "MVT/animales.html", {"lista_animales" : lista_animales})

def crear_statico(request):
    
    Animal(nombre = "Mozart", raza = "Bulldog ingles", edad = 6).save()
    Animal(nombre = "Luna", raza = "Bulldog ingles", edad = 5).save()
    Animal(nombre = "Apolo", raza = "Caniche Toy", edad = 10).save()
    Animal(nombre = "Atena", raza = "Caniche Toy", edad = 10).save()
    Animal(nombre = "Uma", raza = "Caniche Toy", edad = 7).save()
    
    return HttpResponse("Datos guardados")


