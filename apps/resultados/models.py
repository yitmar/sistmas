from django.db import models

# Create your models here.

class resultado(models.Model):
    id_resultado=models.AutoField(primary_key=True)
    id_participante=models.ForeignKey('users.participante',on_delete=models.CASCADE)
    
    id_sub_categoria=models.ForeignKey('categoria.sub_categoria',on_delete=models.CASCADE)
    nota_evaluacion=models.IntegerField()

