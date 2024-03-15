# Generated by Django 3.2.6 on 2024-03-15 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apiBanco', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='apibanco',
            name='apellido',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='apibanco',
            name='contrasenia',
            field=models.CharField(default=1234, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='apibanco',
            name='correo',
            field=models.EmailField(default=1, max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='apibanco',
            name='nombre',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='apibanco',
            name='telefono',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='apibanco',
            name='usuario',
            field=models.CharField(max_length=50),
        ),
    ]
