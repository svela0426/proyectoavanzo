from django import forms
from .models import Solicitud

class SolicitudForm(forms.ModelForm):
    class Meta:
        model = Solicitud
        fields = ['cliente', 'monto', 'fecha', 'cuotas', 'estado']

        labels = {
            'cliente': 'Cliente',
            'monto': 'Monto',
            'fecha': 'Fecha',
            'cuotas': 'Cuotas',
            'estado': 'Estado',
        }
