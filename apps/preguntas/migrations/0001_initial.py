# Generated by Django 2.0.6 on 2018-07-17 19:55

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categoria', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='dificultad',
            fields=[
                ('id_dificultad', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_dificultad', models.CharField(max_length=50, validators=[django.core.validators.RegexValidator(message='solo se acepta solo numero', regex='^[a-zA-z0-9]*S')])),
            ],
        ),
        migrations.CreateModel(
            name='pregunta',
            fields=[
                ('id_pregunta', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_pregunta', models.CharField(max_length=100, validators=[django.core.validators.RegexValidator(message='solo se acepta letras', regex='^[a-zA-Z0-9]*$|\\d*$')])),
                ('dificultad', models.CharField(max_length=150)),
                ('tipo_pregunta', models.CharField(max_length=15)),
                ('pregunta_imagen', models.ImageField(blank=True, null=True, upload_to='')),
                ('id_categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='categoria.categoria')),
            ],
        ),
        migrations.CreateModel(
            name='respuesta',
            fields=[
                ('id_respuesta', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_respuesta', models.CharField(max_length=100, validators=[django.core.validators.RegexValidator(message='solo se acepta letras', regex='^[a-zA-Z]*$|\\d*$')])),
                ('tipo_respuesta', models.BooleanField()),
                ('id_pregunta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='preguntas.pregunta')),
            ],
        ),
        migrations.CreateModel(
            name='tipo_pregunta',
            fields=[
                ('id_tipo_pregunta', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_tipo_pregunta', models.CharField(max_length=20, validators=[django.core.validators.RegexValidator(message='solo se acepta solo numero', regex='^[a-zA-z0-9]*S')])),
            ],
        ),
    ]
