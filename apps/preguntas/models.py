from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

# Create your models here.

class pregunta(models.Model):
    id_pregunta=models.AutoField(primary_key=True)
    id_categoria=models.ForeignKey('categoria.categoria',on_delete=models.CASCADE)
    nombre_pregunta=models.CharField(max_length=100,validators=[
            RegexValidator(
                regex='^[a-zA-Z]*$|\d*$',
                message='solo se acepta letras'
            )
        ])
    valor_pregunta=models.CharField(max_length=2,validators=[
            RegexValidator(
                regex='^[0-9]',
                message='solo se acepta solo numero'
            )
        ])
    dificultad=models.CharField(max_length=150)
    tipo_pregunta=models.CharField(max_length=15)
    pregunta_imagen=models.ImageField()
    
def __str__(self):
    return self.nombre_pregunta
    
class dificultad(models.Model):
    id_dificultad=models.AutoField(primary_key=True)
    nombre_dificultad=models.CharField(max_length=50)

class tipo_pregunta(models.Model):
    id_tipo_pregunta=models.AutoField(primary_key=True)
    id_sub_categoria=models.ForeignKey('categoria.categoria',on_delete=models.CASCADE)
    nombre_tipo_pregunta=models.CharField(max_length=20)

class respuesta(models.Model):
    id_respuesta=models.AutoField(primary_key=True)
    nombre_respuesta=models.CharField(max_length=100,validators=[
            RegexValidator(
                regex='^[a-zA-Z]*$|\d*$',
                message='solo se acepta letras'
            )
        ])
    id_pregunta=models.ForeignKey('pregunta',on_delete=models.CASCADE)
    tipo_respuesta=models.BooleanField()

