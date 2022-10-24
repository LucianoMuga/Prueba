from django.shortcuts import render
from MVT.models import Animal
from django.http import HttpResponse
from MVT.forms import Buscar, AnimalForm
from django.views import View

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

def segundo_estatico(request):
    
    Animal(nombre = "Cachi", raza = "NN", edad = 15).save(),
    Animal(nombre = "topi", raza = "Batata", edad = 17).save(),
    Animal(nombre = "Maxi", raza = "Colie", edad = 16).save(),

    return HttpResponse("Datos guardados")


class BuscarAnimal(View):
    
    form_class = Buscar
    template_name = "MVT/buscar.html"
    initial = {"nombre" : ""}
    
    def get(self, request):
        form = self.form_class(initial= self.initial)
        return render(request, self.template_name, {"form" : form})
    
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data.get("nombre")
            lista_animales = Animal.objects.filter(nombre__icontains = nombre).all()
            form = self.form_class(initial = self.initial)
            return render(request, self.template_name, {"form" : form, 
                                                        "lista_animales" : lista_animales}) 
        return render(request, self.template_name, {"form" : form})        

class AltaAnimal(View):
    
    form_class = AnimalForm
    template_name = "MVT/alta_animal.html"
    initial = {"nombre" : "", "raza" : "", "edad" : ""}
    
    def get(self, request):
        form = self.form_class(initial = self.initial)
        return render(request, self.template_name , {"form" : form})
    
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            msg_exito = f"Se cargo con exito le animal {form.cleaned_data.get('nombre')}"
            form = self.form_class(initial = self.initial)
            return render(request, self.template_name, {'form' : form,
                                                        'msg_extio' : msg_exito})
            
        return render(request, self.template_name, {"form" : form})

          
    