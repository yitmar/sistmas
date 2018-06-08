from django.db import models
from django.core.validators import RegexValidator


# Create your models here.

class participante(models.Model):
    id_participante = models.AutoField(primary_key=True)
    nombres_participante= models.CharField(max_length=50,validators=[
            RegexValidator(
                regex='^[a-zA-Z]*$',
                message='solo se aceptas letras'
            )
        ])
    apellidos_participante= models.CharField(max_length=50,validators=[
            RegexValidator(
                regex='^[a-zA-Z]*$',
                message='solo se aceptas letras'
            )
        ])
    cedula_participante=models.CharField(max_length=9,unique=True,validators=[
            RegexValidator(
                regex='^[0-9]{6,8}',
                message='solo se aceptas letras'
            )
        ])
    tefelono_participante=models.IntegerField()
    correo_participarnte = models.EmailField()
    password= models.CharField(max_length=16)
    tipo_user=models.IntegerField()
    fecha_participacion=models.DateField()
    
    def crear_participante(self, nombres, apellidos, cedula, telefono, correo, *arg, **kwarg):
    
    def __unicode__():
        

