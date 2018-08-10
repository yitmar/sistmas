# Generated by Django 2.0.6 on 2018-08-10 18:53

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='categoria',
            fields=[
                ('id_categoria', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_categoria', models.CharField(max_length=50, unique=True, validators=[django.core.validators.RegexValidator(message='no acepta caracteres especiales ', regex='^[a-zA-z0-9\\s]*$')])),
                ('descripcion_categoria', models.CharField(default='', max_length=100, validators=[django.core.validators.RegexValidator(message='solo acepta letras', regex='^[a-zA-z\\s]*$')])),
            ],
        ),
        migrations.CreateModel(
            name='sub_categoria',
            fields=[
                ('id_subcategoria', models.AutoField(primary_key=True, serialize=False)),
                ('id_categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='categoria.categoria')),
            ],
        ),
    ]
