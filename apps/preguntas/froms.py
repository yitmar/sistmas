from django import forms

from .models import pregunta, respuesta

lista_tipo_pregunta= (('1', 'seleccion simple',), ('2', 'seleccion multiple',))
lista_dificultad=(('1','basico',),('2','intermedia',),('3','avanzada',))

class preguntas_form(forms.ModelForm):
    tipo_pregunta = forms.ChoiceField(widget=forms.RadioSelect, choices=lista_tipo_pregunta)
    dificultad = forms.ChoiceField(widget=forms.RadioSelect, choices=lista_dificultad)
    
    class Meta:
        model=pregunta
        fields=("nombre_pregunta","dificultad","tipo_pregunta","id_categoria")

class respuesta_from(forms.ModelForm):
    
    lista_tipo_respuesta=(('True',' verdadera',),('False','falsa'))
    tipo_respuesta=forms.ChoiceField(widget=forms.RadioSelect, choices=lista_tipo_respuesta)

    class Meta:
        model=respuesta
        fields=("id_pregunta","nombre_respuesta","tipo_respuesta")