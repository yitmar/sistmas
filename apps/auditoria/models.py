from django.db import models

# Create your models here.


class auditoria(models.Model):
    id_auditoria=models.AutoField(primary_key=True)
    id_usuario=models.IntegerField()
    fecha_auditoria=models.DateField()
    modulo=models.CharField(max_length=20)
    direccion_ip=models.GenericIPAddressField()


