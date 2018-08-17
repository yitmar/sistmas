from django import forms

from apps.preguntas.models import dificultad, pregunta
from apps.categoria.models import categoria
from apps.resultados.models import resultado
from apps.inicio.models import user as  User

from .models import prueba, prueba_presona 

class formulario_crear_prueba(forms.ModelForm):
    class Meta:
        model=prueba
        fields=('nombre_prueba','durancion_pruaba','valor_prueba','cantidad_pregunta')
        widgets={
            'valor_prueba':forms.TextInput(),
            'durancion_pruaba':forms.TextInput(),
            'cantidad_pregunta':forms.TextInput(),
        }
        help_texts={
            'durancion_pruaba':'la duracion de tiemṕo de prueba tiene que ser es en  minutos',
        }
     
class formulario_realizar_prueba(forms.ModelForm):
    class Meta:
        model=resultado
        fields=('__all__')
