from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

# Create your models here.

class pregunta(models.Model):
    id_pregunta=models.AutoField(primary_key=True)
    nombre_pregunta=models.CharField(max_length=100)
    valor_pregunta=models.IntegerField()
    id_dificultad=models.ForeignKey('dificultad',on_delete=models.CASCADE)
    id_tipo_pregunta=models.ForeignKey('tipo_pregunta',on_delete=models.CASCADE)
    pregunta_imagen=models.ImageField()

class dificultad(models.Model):
    id_dificultad=models.AutoField(primary_key=True)
    nombre_dificultad=models.CharField(max_length=50)

class tipo_pregunta(models.Model):
    id_tipo_pregunta=models.AutoField(primary_key=True)
    id_sub_categoria=models.ForeignKey('categoria.categoria',on_delete=models.CASCADE)
    nombre_tipo_pregunta=models.CharField(max_length=20)

class respuesta(models.Model):
    id_respuesta=models.AutoField(primary_key=True)
    nombre_respuesta=models.CharField(max_length=100)
    id_pregunta=models.ForeignKey('pregunta',on_delete=models.CASCADE)
    tipo_respuesta=models.BooleanField()

