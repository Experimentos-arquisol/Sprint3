# Generated by Django 3.2.6 on 2024-04-10 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ManejadorSolicitudes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profesion', models.CharField(max_length=50)),
                ('actividad_economica', models.CharField(max_length=50)),
                ('empresa', models.CharField(max_length=50)),
                ('ingresos', models.BigIntegerField()),
                ('deudas', models.BigIntegerField()),
            ],
        ),
    ]