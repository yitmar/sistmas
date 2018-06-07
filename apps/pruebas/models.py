from django.db import models

# Create your models here.
class prueba(models.Model):
    id_prueba=models.AutoField(primary_key=True)
    tipo_prueba=models.CharField(max_length=50)
    durancion_pruaba=models.IntegerField()
    