# Generated by Django 2.0.6 on 2018-08-02 18:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_participante_is_participante'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participante',
            name='is_participante',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
