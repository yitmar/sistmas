from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import RegexValidator

from .models import user as User

class forms_login(forms.Form):
    cedula=forms.CharField(validators=[
            RegexValidator(
                regex='^[0-9]{6,8}',
                message='solo se aceptas numeros y deben ser entre 6 a 8'
            )
        ])
    password= forms.CharField(widget=forms.PasswordInput())

class formulario_registero_particpante(UserCreationForm):
    
    class Meta(UserCreationForm.Meta):
        model = User
        fields=('nombre_usuario','apellidos_usuario','correo_usuario','celuda_usuario','tefelono_usuario')

    def save(self):
        user = super().save(commit=False)
        user.is_participante = True
        user.save()
        return user
        
class formilario_registro_instructor(UserCreationForm):
    
    class Meta(UserCreationForm.Meta):
        model = User
        fields=('nombre_usuario','apellidos_usuario','correo_usuario','p00','celuda_usuario','tefelono_usuario')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_instructor = True
        if commit:
            user.save()
        return user

