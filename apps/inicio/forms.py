from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import password_validation
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _

from .models import user as User

class forms_login(forms.Form):
    cedula=forms.CharField(validators=[
            RegexValidator(
                regex='^[0-9]{6,8}',
                message='solo se aceptas numeros y deben ser entre 6-8'
            )
        ])
    password= forms.CharField(widget=forms.PasswordInput())

class formulario_registero_particpante(UserCreationForm):
    
    class Meta(UserCreationForm.Meta):
        model = User
        fields=('nombre_usuario','apellidos_usuario','email','cedula_usuario','tefelono_usuario')
        widgets = {
            'cedula_usuario': forms.TextInput(attrs={'cols': 80, 'rows': 20}),
        }
        help_texts = {
            'password1': password_validation.password_validators_help_text_html(),
        }

    def save(self):
        user = super().save(commit=False)
        user.is_participante = True
        user.save()
        return user
        
class formilario_registro_instructor(UserCreationForm):
    
    class Meta(UserCreationForm.Meta):
        model = User
        fields=('nombre_usuario','apellidos_usuario','email','p00','cedula_usuario','tefelono_usuario')
        widgets = {
            'cedula_usuario': forms.TextInput(attrs={'cols': 80, 'rows': 20}),
            'p00':forms.TextInput(),
        }
        help_texts = {
            'password1': password_validation.password_validators_help_text_html(),
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_instructor = True
        user.save()
        return user
