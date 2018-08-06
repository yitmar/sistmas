from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.core.validators import RegexValidator



# Create your models here.

class usermanager(BaseUserManager):

    def crear_user(self, celuda_usuario, password):
        user=self.model(celuda_usuario=celuda_usuario)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, celuda_usuario, password):
        admin=self.crear_user(celuda_usuario,password)
        admin.is_staff= True
        admin.is_superuser=True
        admin.save(using=self._db)
        return admin

    def crear_participante(self,celuda_usuario,password):
        particante=self.model(celuda_usuario,password)
        particante.is_participante=True
        particante.save(using=self._db)
        return particante

    def crear_instructor(self,celuda_usuario,password):
        instructor=self.model(celuda_usuario,password)
        instructor.is_instructor=True
        instructor.save(using=self._db)
        return instructor

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

    correo_usuario=models.EmailField(validators=[
            RegexValidator(
                regex='^[a-zA-Z]*@hotmail.com|[a-zA-Z]*@gmail.com$',
                message='solo se permiten correos hotmail.com o gmail.com'
            )
        ])

    fecha_participacion=models.DateField(auto_now=True)

    p00=models.IntegerField(unique=True, blank=True, null=True, validators=[
            RegexValidator(
                regex='^[0-9]{6,8}',
                message='solo se aceptas numeros'
            )
        ])
    celuda_usuario=models.IntegerField(unique=True, validators=[
            RegexValidator(
                regex='^[0-9]{6,8}',
                message='solo se aceptas numeros'
            )
        ])

    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)
    is_participante=models.BooleanField(default=False)
    id_instructor=models.BooleanField(default=False)

    USERNAME_FIELD='celuda_usuario'
    REQUIRED_FIELD=['celuda_usuario','password']

    objects= usermanager()

    def __str__(self):
        return '{} {}'.format(self.nombre_usuario, self.apellidos_usuario)