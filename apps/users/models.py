from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class participante(models.Model):
    id_participante = models.AutoField(primary_key=True)
    nombres_participante= models.CharField(max_length=50,validators=[
            RegexValidator(
                regex='^[a-zA-Z]*$|\d*$',
                message='solo se aceptas letras'
            )
        ])
    apellidos_participante= models.CharField(max_length=50,validators=[
            RegexValidator(
                regex='^[a-zA-Z]*$|\d*$',
                message='solo se aceptas letras'
            )
        ])
    cedula_participante=models.CharField(max_length=9,unique=True,validators=[
            RegexValidator(
                regex='^[0-9]{6,8}',
                message='solo se aceptas numeros'
            )
        ])
    tefelono_participante=models.CharField(max_length=11,validators=[
            RegexValidator(
               regex='^[0-9]{11}',
               message='el campo acepta solo numeros', 
            )
        ])
    correo_participarnte = models.EmailField(validators=[
            RegexValidator(
                regex='^[a-zA-Z]*@hotmail.com|[a-zA-Z]*@gmail.com$',
                message='solo se permiten correos hotmail.com o gmail.com'
            )
        ])
    fecha_participacion=models.DateField(auto_now=True)

def __str__ (self):
    return self.nombres_participante


