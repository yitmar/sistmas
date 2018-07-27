from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


# Create your models here.

class usermanager(BaseUserManager):

    def crear_user(self, p00, password):
        user=self.model(p00=p00)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, p00,password):
        admin=self.crear_user(p00,password)
        admin.is_staff= True
        admin.is_superuser=True
        admin.save(using=self._db)
        return admin

class administrador(AbstractBaseUser,PermissionsMixin):
    id_admin= models.AutoField(primary_key=True)
    nombre_admin= models.CharField(max_length=50)
    apellidos_admin= models.CharField(max_length=50)
    p00=models.IntegerField(unique=True)

    is_active= models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)
    
    USERNAME_FIELD='p00'
    REQUIRED_FIELD=['p00','password']

    objects= usermanager()

    def get_short_name(self):
        return self.nombre_admin