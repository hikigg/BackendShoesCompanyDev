# Generated by Django 4.2.7 on 2023-11-30 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalusuario',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Nombre'),
        ),
        migrations.AddField(
            model_name='usuario',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Nombre'),
        ),
    ]
