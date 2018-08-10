from django.db import models
from django.contrib.postgres.fields import ArrayField


# Create your models here.

class resultado(models.Model):
    id_resultado=models.AutoField(primary_key=True)
    id_admin=models.ForeignKey('inicio.user',on_delete=models.CASCADE)
    id_categoria=models.ForeignKey('categoria.categoria',on_delete=models.CASCADE)
    arreglo_preguntas=ArrayField(models.CharField( max_length=100),blank=True)
    arreglo_respuesta=ArrayField(models.IntegerField(),blank=True)
    nota_evaluacion=models.IntegerField()
    fecha_presentacion=models.DateField(auto_now=True)
    
    def __str__(self):
        return self.id_resultado
