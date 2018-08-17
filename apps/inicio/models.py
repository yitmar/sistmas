from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.core.validators import RegexValidator

# Create your models here.

class usermanager(BaseUserManager):

    def crear_user(self, cedula_usuario, password):
        user=self.model(cedula_usuario=cedula_usuario)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, cedula_usuario, password):
        admin=self.crear_user(cedula_usuario,password)
        admin.is_staff= True
        admin.is_superuser=True
        admin.save(using=self._db)
        return admin


class user(AbstractBaseUser,PermissionsMixin):
    
    id_admin=models.AutoField(primary_key=True)
    
    nombre_usuario=models.CharField(max_length=50,validators=[
            RegexValidator(
                regex='^[a-zA-Z]*$|\d*$',
                message='solo se aceptas letras'
            )
        ])
    apellidos_usuario=models.CharField(max_length=50,validators=[
            RegexValidator(
                regex='^[a-zA-Z]*$|\d*$',
                message='solo se aceptas letras'
            )
        ])
    tefelono_usuario=models.CharField(max_length=11,validators=[
            RegexValidator(
               regex='^[0-9]{11}',
               message='el campo acepta solo numeros', 
            )
        ])

    email=models.EmailField()

    fecha_participacion=models.DateField(auto_now=True)

    p00=models.IntegerField(unique=True, blank=True, null=True, validators=[
            RegexValidator(
                regex='^[0-9]{6,8}',
                message='solo se aceptas numeros'
            )
        ])
    cedula_usuario=models.IntegerField(unique=True, validators=[
            RegexValidator(
                regex='^[0-9]{6,8}',
                message='solo se aceptas numeros'
            )
        ])

    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)
    is_participante=models.BooleanField(default=False)
    is_instructor=models.BooleanField(default=False)

    USERNAME_FIELD='cedula_usuario'
    REQUIRED_FIELD=['cedula_usuario','password']

    objects= usermanager()

    def __str__(self):
        return '{}'.format(self.cedula_usuario) 