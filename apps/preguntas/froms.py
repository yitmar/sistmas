from .models import pregunta, respuesta
from django import forms

lista_tipo_pregunta= (('1', 'seleccion simple',), ('2', 'seleccion multiple',))
lista_dificultad=(('1','avanzada',),('2','intermedia',),('3','basico',))


class preguntas_form(forms.ModelForm):
    tipo_pregunta = forms.ChoiceField(widget=forms.RadioSelect, choices=lista_tipo_pregunta)
    dificultad = forms.ChoiceField(widget=forms.RadioSelect, choices=lista_dificultad)
    
    class Meta:
        model=pregunta
        fields=("nombre_pregunta","valor_pregunta","dificultad","tipo_pregunta","id_categoria")



class respuesta_from(forms.ModelForm):
    id_pregunta=forms.ModelChoiceField(queryset=pregunta.objects.all())
    
    lista_tipo_respuesta=(('True',' verdadera',),('Flase','falsa'))
    tipo_respuesta=forms.ChoiceField(widget=forms.RadioSelect, choices=lista_tipo_respuesta)

    class Meta:
        model=respuesta
        fields=("id_pregunta","nombre_respuesta","tipo_respuesta")
