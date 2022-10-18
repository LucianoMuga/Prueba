from django.shortcuts import render
from MVT.models import Animal

def index(request):
    return render(request, "MVT/index.html")


def mostrarAnimal(request):
    lista_animales = Animal.objects.all()
    return render(request, "MVT/animales.html", {"Lista_animales" : lista_animales})
