# Generated by Django 2.0.6 on 2018-06-14 20:42

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('categoria', '0002_auto_20180613_1848'),
        ('preguntas', '0003_auto_20180614_1814'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pregunta',
            name='id_dificultad',
        ),
        migrations.RemoveField(
            model_name='pregunta',
            name='id_tipo_pregunta',
        ),
        migrations.AddField(
            model_name='pregunta',
            name='dificultad',
            field=models.CharField(default=1458, max_length=150, validators=[django.core.validators.RegexValidator(message='solo se acepta letras', regex='^[a-zA-Z]*$')]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pregunta',
            name='id_categoria',
            field=models.ForeignKey(default=12345678, on_delete=django.db.models.deletion.CASCADE, to='categoria.categoria'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pregunta',
            name='tipo_pregunta',
            field=models.CharField(default=123456, max_length=15, validators=[django.core.validators.RegexValidator(message='solo se acepta letras', regex='^[a-zA-Z]*$')]),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='pregunta',
            name='nombre_pregunta',
            field=models.CharField(max_length=100, validators=[django.core.validators.RegexValidator(message='solo se acepta letras', regex='^[a-zA-Z]*$|\\d*$')]),
        ),
        migrations.AlterField(
            model_name='pregunta',
            name='valor_pregunta',
            field=models.CharField(max_length=2, validators=[django.core.validators.RegexValidator(message='solo se acepta solo numero', regex='^[0-9]')]),
        ),
        migrations.AlterField(
            model_name='respuesta',
            name='nombre_respuesta',
            field=models.CharField(max_length=100, validators=[django.core.validators.RegexValidator(message='solo se acepta letras', regex='^[a-zA-Z]*$|\\d*$')]),
        ),
    ]
