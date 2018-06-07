from django.db import models


# Create your models here.

class participante(models.Model):
    id_participante = models.AutoField(primary_key=True)
    nombres_participante= models.CharField(max_length=50)
    apellidos_participante= models.CharField(max_length=50)
    cedula_participante=models.CharField(max_length=9,unique=True)
    tefelono_participante=models.IntegerField()
    correo_participarnte = models.EmailField()
    password= models.CharField(max_length=16)
    tipo_user=models.IntegerField()
    fecha_participacion=models.DateField()
    
