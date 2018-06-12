# Generated by Django 2.0.6 on 2018-06-12 20:19

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='participante',
            fields=[
                ('id_participante', models.AutoField(primary_key=True, serialize=False)),
                ('nombres_participante', models.CharField(max_length=50, validators=[django.core.validators.RegexValidator(message='solo se aceptas letras', regex='^[a-zA-Z]*$')])),
                ('apellidos_participante', models.CharField(max_length=50, validators=[django.core.validators.RegexValidator(message='solo se aceptas letras', regex='^[a-zA-Z]*$')])),
                ('cedula_participante', models.CharField(max_length=9, unique=True, validators=[django.core.validators.RegexValidator(message='solo se aceptas letras', regex='^[0-9]{6,8}')])),
                ('tefelono_participante', models.IntegerField(validators=[django.core.validators.RegexValidator(message='el campo acepta solo letras', regex='^[0-9]{10}')])),
                ('correo_participarnte', models.EmailField(max_length=254, validators=[django.core.validators.RegexValidator(message='solo se permiten correos hotmail.com o gmail.com', regex='^[a-zA-Z]*@hotmail.com|[a-zA-Z]*@gmail.com$')])),
                ('fecha_participacion', models.DateField()),
            ],
        ),
    ]
