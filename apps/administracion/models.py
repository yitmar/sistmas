from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.core.validators import RegexValidator


# Create your models here.

class usermanager(BaseUserManager):

    def crear_user(self, p00, password):
        user=self.model(p00=p00)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, p00, password):
        admin=self.crear_user(p00,password)
        admin.is_staff= True
        admin.is_superuser=True
        admin.save(using=self._db)
        return admin

    def crear_participante(self,p00,password):
        particante=self.model(p00,password)
        particante.is_participante=True
        particante.save(using=self._db)
        return particante

    def crear_instructor(self,p00,password):
        instructor=self.model(p00,password)
        instructor.is_participante=True
        instructor.save(using=self._db)
        return instructor

class administrador(AbstractBaseUser,PermissionsMixin):
    id_admin=models.AutoField(primary_key=True)
    
    nombre_user=models.CharField(max_length=50,validators=[
            RegexValidator(
                regex='^[a-zA-Z]*$|\d*$',
                message='solo se aceptas letras'
            )
        ])
    apellidos_users=models.CharField(max_length=50,validators=[
            RegexValidator(
                regex='^[a-zA-Z]*$|\d*$',
                message='solo se aceptas letras'
            )
        ])

    p00=models.IntegerField(unique=True,validators=[
            RegexValidator(
                regex='^[0-9]{6,8}',
                message='solo se aceptas numeros'
            )
        ])
    celuda=models.IntegerField(unique=True)

    correo_participarnte=models.EmailField(validators=[
            RegexValidator(
                regex='^[a-zA-Z]*@hotmail.com|[a-zA-Z]*@gmail.com$',
                message='solo se permiten correos hotmail.com o gmail.com'
            )
        ])

    fecha_participacion=models.DateField(auto_now=True)

    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)
    is_participante=models.BooleanField(default=False)
    id_instructor=models.BooleanField(default=False)

    USERNAME_FIELD='p00'
    REQUIRED_FIELD=['p00','password']

    objects= usermanager()

    def get_short_name(self):
        return self.nombre_user