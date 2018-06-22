from django.db import models
from django.core.validators import RegexValidator
from django.contrib.postgres.fields import ArrayField
# Create your models here.
class prueba(models.Model):
    id_prueba=models.AutoField(primary_key=True)
    id_participante=models.ForeignKey('users.participante',on_delete=models.CASCADE)
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
    arreglo_valor=ArrayField(models.IntegerField(),blank=True)
    
    def __str__(self):
        return self.id_prueba
