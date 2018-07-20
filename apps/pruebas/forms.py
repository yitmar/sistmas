from django import forms
from apps.preguntas.models import dificultad, pregunta
from apps.categoria.models import categoria
from apps.administracion.models import administrador
from apps.resultados.models import resultado
from .models import prueba, prueba_presona

class formulario_asignar_prueba(forms.ModelForm):        
    class Meta:
        model=prueba_presona
        #fields=('nombre_prueba','id_categoria','id_dificultad','tipo_prueba','durancion_pruaba','valor_prueba','cantidad_pregunta')
        fields=('__all__')


class formulario_crear_prueba(forms.ModelForm):
    #PREGUNTAS = forms.ModelMultipleChoiceField(queryset=pregunta.objects.all(), widget=forms.CheckboxSelectMultiple)
    class Meta:
        model=prueba
        fields=('nombre_prueba','durancion_pruaba','valor_prueba','cantidad_pregunta')
     
class formulario_realizar_prueba(forms.ModelForm):
    class Meta:
        model=resultado
        fields=('__all__')


# nombre_prueba 
# id_categoria
# id_dificultad
# durancion_pruaba
# valor_prueba
# cantidad_pregunta
# tipo_prueba
# arreglo_preguntas
# arreglo_valor
