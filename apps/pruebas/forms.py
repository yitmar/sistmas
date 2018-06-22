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
"""
    id_prueba=models.AutoField(primary_key=True)
    id_participante=models.ForeignKey('users.participante',on_delete=models.CASCADE)
    id_categoria=models.ForeignKey('categoria.categoria',on_delete=models.CASCADE)    
    id_dificultad=models.ForeignKey('preguntas.dificultad',on_delete=models.CASCADE)
    durancion_pruaba=models.IntegerField()
    valor_prueba=models.IntegerField()
    cantidad_pregunta=models.IntegerField()
    tipo_prueba=models.CharField(max_length=50)    
    arreglo_preguntas=ArrayField(ArrayField(models.IntegerField()))
"""
class formulario_crear_prueba(forms.ModelForm):
    preguntas = forms.ModelMultipleChoiceField(queryset=pregunta.objects.all(), widget=forms.CheckboxSelectMultiple)    
    lista=[]
    lista.append(1)
    print (lista)
    """for a in conte:
        lista=[]
        print(a)
        queryset=(int(a.objects.id_pregunta),str(a.nombre_pregunta),)
        lista.append(queryset)  
    """
    #preguntas = ArrayField(models.IntegerField(),default=[], blank=True, choices=(elemento)
    #print elemento
    class Meta:
        model=prueba
        #fields=('id_participante','id_categoria','id_dificultad','durancion_pruaba','valor_prueba','cantidad_pregunta','preguntas')
        fields=('__all__')
"""
    class form_prueba_prueba(forms.Form):
        id_categorias = forms.ModelChoiceField(
            label=u'categoria', 
            queryset=categoria.objects.all()
        )
        id_dificul = forms.ModelChoiceField(
            label=u'dificultad', 
            queryset=dificultad.objects.all()
        )
        lista_prguntas=forms.ModelChoiceField(
            label=u'pretungas',
            queryset=prueba.objects.all()
        )
        nombre_de_intructor=forms.ModelChoiceField(
            label=u'intructor',
            queryset=administrador.objects.all()
        )

        def__init__(self, *args, **kwargs):
            super(form_prueba_prueba, self).__init__(*args, **kwargs)
            self.fields['id_categorias'].queryset = categoria.objects.none()
            self.fields['id_dificul'].queryset = dificultad.objects.none()
"""
class formulario_realizar_prueba(forms.ModelForm):

    class Meta:
        model=resultado
        fields=("__all__")
