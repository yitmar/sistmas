from .models import participante
from django import forms

class participante_form(forms.ModelForm):
    class Meta:
        model=participante
        fields=('nombres_participante','apellidos_participante','cedula_participante','correo_participarnte')
        
    
    """
    nombres_participante=forms.CharField(max_length=50, required=True)
    apellidos_participante=forms.CharField(max_length=50, required=True)
    """
    """
    cedula_participante
    tefelono_participante
    correo_participarnte
        ['','','','','']
"""
 #<input placeholder="Nombres" type="text" name="name" id="nombres" size="30" value="" required/>

#insert
#form= participante_form()

#update
#article=participante.objects.get(pk=1)
#form= participante_form(instance=article )

    