# Generated by Django 2.0.6 on 2018-08-02 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administracion', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='administrador',
            name='id_instructor',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='administrador',
            name='is_participante',
            field=models.BooleanField(default=False),
        ),
    ]
