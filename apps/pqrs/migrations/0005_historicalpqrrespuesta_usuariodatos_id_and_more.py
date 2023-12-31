# Generated by Django 4.2.7 on 2023-12-02 08:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0004_historicalusuariodatos_documento_and_more'),
        ('pqrs', '0004_alter_historicalpqrrespuesta_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalpqrrespuesta',
            name='usuariodatos_id',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='usuarios.usuariodatos', verbose_name='Datos del usuario para la peticion'),
        ),
        migrations.AddField(
            model_name='pqrrespuesta',
            name='usuariodatos_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='usuarios.usuariodatos', verbose_name='Datos del usuario para la peticion'),
        ),
    ]
