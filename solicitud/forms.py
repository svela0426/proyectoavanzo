from django import forms
from .models import Solicitud

class SolicitudForm(forms.ModelForm):
    class Meta:
        model = Solicitud
        fields = ['Cliente', 'monto', 'fecha', 'cuotas', 'estado']

        labels = {
            'Cliente': 'Cliente',
            'monto': 'Monto',
            'fecha': 'Fecha',
            'cuotas': 'Cuotas',
            'estado': 'Estado',
        }
