from django import forms
from MVT.models import Animal, Empleado, Cliente

class Buscar(forms.Form):
    nombre = forms.CharField(max_length=100)
    
class AnimalForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields = ['nombre', 'raza', 'edad']
        
class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = ['nombre', 'area', 'años_de_antiguedad']

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'producto', 'numero_de_cliente']