# Generated by Django 2.0.6 on 2018-06-05 20:25

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
                ('nombres_participante', models.CharField(max_length=50)),
                ('apellidos_participante', models.CharField(max_length=50)),
                ('cedula_participante', models.CharField(max_length=9, unique=True)),
                ('tefelono_participante', models.IntegerField()),
                ('correo_participarnte', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=16)),
                ('tipo_user', models.IntegerField()),
                ('fecha_participacion', models.DateField()),
            ],
        ),
    ]