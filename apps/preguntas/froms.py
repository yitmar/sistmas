from django import forms
from apps.categoria.models import  categoria

from .models import pregunta, respuesta

lista_tipo_pregunta= (('1', 'seleccion simple',), ('2', 'seleccion multiple',))
lista_dificultad=(('1','basico',),('2','intermedia',),('3','avanzada',))

class preguntas_form(forms.ModelForm):

    tipo_pregunta = forms.ChoiceField(widget=forms.RadioSelect, choices=lista_tipo_pregunta)
    class Meta:
        model=pregunta
        fields=("nombre_pregunta","tipo_pregunta")


class respuesta_from(forms.ModelForm):
    
    lista_tipo_respuesta=(('True',' verdadera',),('False','falsa'))
    tipo_respuesta=forms.ChoiceField(widget=forms.RadioSelect, choices=lista_tipo_respuesta)
    class Meta:
        model=respuesta
        fields=("nombre_respuesta","tipo_respuesta")