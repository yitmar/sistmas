from django import forms
from apps.preguntas.models import dificultad, pregunta
from apps.categoria.models import categoria
from apps.administracion.models import administrador
from apps.resultados.models import resultado
from .models import prueba

class formulario_asignar_prueba(forms.ModelForm):    
    lista_seleccion_de_prueba=(('0','personalizada'),('1','estandar')) 
    tipo_prueba=forms.ChoiceField(widget=forms.RadioSelect,choices=lista_seleccion_de_prueba)        
      
    class Meta:
        model=prueba
        fields=('id_participante','id_categoria','id_dificultad','tipo_prueba','durancion_pruaba','valor_prueba','cantidad_pregunta')

class formulario_crear_prueba(forms.ModelForm):
    #PREGUNTAS = forms.ModelMultipleChoiceField(queryset=pregunta.objects.all(), widget=forms.CheckboxSelectMultiple)
    preguntas=pregunta.objects.all()
    lista_preguntas=[]
    for pre in preguntas:
        id_pre=pre.id_pregunta            
        nombre_pregunta=pre.nombre_pregunta
        listaaa=(id_pre,nombre_pregunta)
        lista_preguntas.append(listaaa)
    print(lista_preguntas)
    PREGUNTAS=forms.ChoiceField(widget=forms.CheckboxSelectMultiple, choices=lista_preguntas)
    class Meta:
        model=prueba
        fields=('id_participante','id_categoria','id_dificultad','durancion_pruaba','valor_prueba','cantidad_pregunta',"PREGUNTAS")
        #fields=('__all__')

class formulario_realizar_prueba(forms.ModelForm):
    class Meta:
        model=resultado
        fields=('__all__')
#id_participante,   id_categoria,   arreglo_preguntas,  arreglo_respuesta,  nota_evaluacion