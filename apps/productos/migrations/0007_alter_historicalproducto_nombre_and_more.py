# Generated by Django 4.2.7 on 2023-12-04 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0006_alter_historicalproducto_color_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalproducto',
            name='nombre',
            field=models.CharField(db_index=True, max_length=150, verbose_name='Nombre de producto'),
        ),
        migrations.AlterField(
            model_name='imagenesproducto',
            name='image',
            field=models.ImageField(blank=True, max_length=255, null=True, upload_to='productos/', verbose_name='Imagen de producto'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='nombre',
            field=models.CharField(max_length=150, unique=True, verbose_name='Nombre de producto'),
        ),
    ]