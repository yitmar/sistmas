from django import forms
from .models import categoria


class nueva_categoria_form(forms.ModelForm):
    class Meta:
        model=categoria
        fields=('nombre_categoria','descripcion_categoria')

