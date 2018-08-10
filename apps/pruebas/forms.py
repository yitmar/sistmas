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
     
class formulario_realizar_prueba(forms.ModelForm):
    class Meta:
        model=resultado
        fields=('__all__')

class formulario_asignar_prueba(forms.ModelForm):
    try:
        pruebas=prueba.objects.all()
        lista_pruebas=[]
        for prue in pruebas:
            id_prueb=prue.id_prueba            
            nombre_prueba=prue.nombre_prueba
            listaaa=(id_prueb,nombre_prueba)
            lista_pruebas.append(listaaa)
        id_prueba=forms.ChoiceField(widget=forms.Select, choices=lista_pruebas)

        useuarios=User.objects.all()
        lista_usuarios=[]
        for prue in useuarios:
            id_admin=prue.cedula_usuario            
            nombre_usuario=prue.nombre_usuario
            listaa=(id_admin,nombre_usuario)
            lista_usuarios.append(listaa)
            id_admin=forms.ChoiceField(widget=forms.Select, choices=lista_usuarios)

    except:
        print("no se an creado los modelos ")
   
    
    class Meta:
        model=prueba_presona
        #fields=('nombre_prueba','id_categoria','id_dificultad','tipo_prueba','durancion_pruaba','valor_prueba','cantidad_pregunta')
        fields=('id_admin','id_prueba')


