from .models import participante
from django import forms


class participante_form(forms.ModelForm):
    class Meta:
        model=participante
        fields=('nombres_participante','apellidos_participante','cedula_participante','tefelono_participante','correo_participarnte')