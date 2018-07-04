from django import forms
from django.core.validators import RegexValidator

class formulario_cedula(forms.ModelForm):
    cedula=forms.CharField(label='indique la cedula', max_length=8)
        