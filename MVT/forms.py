from django import forms
from MVT.models import Animal

class Buscar(forms.Form):
    nombre = forms.CharField(max_length=100)
    
class AnimalForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields = ['nombre', 'raza', 'edad']
