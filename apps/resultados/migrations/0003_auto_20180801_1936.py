# Generated by Django 2.0.6 on 2018-08-01 19:36

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resultados', '0002_resultado_fecha_presentacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resultado',
            name='arreglo_preguntas',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=50), blank=True, size=None),
        ),
    ]
