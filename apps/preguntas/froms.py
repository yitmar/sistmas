from django import forms
from apps.categoria.models import  categoria

from .models import pregunta, respuesta

lista_tipo_pregunta= (('1', 'seleccion simple',), ('2', 'seleccion multiple',))
lista_dificultad=(('1','basico',),('2','intermedia',),('3','avanzada',))

class preguntas_form(forms.ModelForm):

    categorias=categoria.objects.all()
    lista_categorias=[]
    for cate in categorias:
        id_cate=cate.id_categoria
        nombre_cate=cate.nombre_categoria
        tuplas=(id_cate,nombre_cate)
        lista_categorias.append(tuplas)

    tipo_pregunta = forms.ChoiceField(widget=forms.RadioSelect, choices=lista_tipo_pregunta)
    dificultad = forms.ChoiceField(widget=forms.RadioSelect, choices=lista_dificultad)
    id_categoria = forms.ChoiceField(widget=forms.RadioSelect, choices=lista_categorias)
    
    class Meta:
        model=pregunta
        fields=("nombre_pregunta","dificultad","tipo_pregunta","id_categoria")

class respuesta_from(forms.ModelForm):
    
    lista_tipo_respuesta=(('True',' verdadera',),('False','falsa'))
    tipo_respuesta=forms.ChoiceField(widget=forms.RadioSelect, choices=lista_tipo_respuesta)
    preguntas=pregunta.objects.all()
    lista_pregunta=[]

    class Meta:
        model=respuesta
        fields=("id_pregunta","nombre_respuesta","tipo_respuesta")