from django.db import models
from django.core.validators import RegexValidator
from django.contrib.postgres.fields import ArrayField

from apps.preguntas.models import pregunta as Pregunta
from apps.users.models import participante as Participante
from apps.inicio.models import user as User


# Create your models here.
class prueba(models.Model):
    id_prueba=models.AutoField(primary_key=True)
    nombre_prueba=models.CharField(max_length=50)    
    id_categoria=models.ForeignKey('categoria.categoria',on_delete=models.CASCADE)    
    id_dificultad=models.ForeignKey('preguntas.dificultad',on_delete=models.CASCADE)
    durancion_pruaba=models.IntegerField(validators=[
            RegexValidator(
                regex='^[0-9]{0,2}',
                message='solo se acepta solo numero'
            )
        ])
    valor_prueba=models.IntegerField(validators=[
            RegexValidator(
                regex='^[0-9]{0,2}',
                message='solo se acepta solo numero'
            )
        ])
    cantidad_pregunta=models.IntegerField(validators=[
            RegexValidator(
                regex='^[0-9]{0,2}',
                message='solo se acepta solo numero'
            )
        ])
    tipo_prueba=models.CharField(max_length=50,blank=True)    
    arreglo_preguntas=ArrayField(models.IntegerField(), blank=True)
    arreglo_valor=ArrayField(models.IntegerField(), blank=True)
    
    def __str__(self):
        return self.id_prueba

class prueba_presona(models.Model):
    id_prueba_presona=models.AutoField(primary_key=True)
    id_admin=models.IntegerField()
    id_prueba=models.IntegerField()
    
    def __str__(self):
        return '{}'.format(self.id_prueba_presona) 