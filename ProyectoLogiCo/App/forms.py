from django import forms
from .models import Farmacia, Moto, Motorista

class FarmaciaForm(forms.ModelForm):
    class Meta:
        model = Farmacia
        fields = ['nombre', 'direccion', 'telefono', 'correo']


class MotoForm(forms.ModelForm):
    class Meta:
        model = Moto
        fields = ['patente', 'marca', 'modelo', 'anio', 'tipo', 'disponible']


class MotoristaForm(forms.ModelForm):
    class Meta:
        model = Motorista
        fields = ['nombre', 'rut', 'telefono', 'correo', 'licencia', 'estado', 'moto', 'farmacia', 'fecha_ingreso']
        widgets = {
            'fecha_ingreso': forms.DateInput(attrs={'type': 'date'}),
        }