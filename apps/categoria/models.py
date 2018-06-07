from django.db import models

# Create your models here.

class categoria(models.Model):
    id_categoria=models.AutoField(primary_key=True)
    nombre_categoria=models.CharField(max_length=50)

class sub_categoria(models.Model):
    id_subcategoria=models.AutoField(primary_key=True)
    id_categoria=models.ForeignKey('categoria',on_delete=models.CASCADE)

