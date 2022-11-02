from django.shortcuts import render
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from MVT.models import Animal, Empleado, Cliente

class AnimalList(ListView):
    model = Animal
    
class AnimalCrear(CreateView):
    model = Animal
    success_url = "/panel-app"
    fields = ["nombre", "raza", "edad"]
    
class AnimalBorrar(DeleteView):
  model = Animal
  success_url = "/panel-app"
  
class AnimalActualizar(UpdateView):
    model = Animal
    success_url = "/panel-app"
    fields = ["nombre", "direccion", "numero_pasaporte"]

# Create your views here.
