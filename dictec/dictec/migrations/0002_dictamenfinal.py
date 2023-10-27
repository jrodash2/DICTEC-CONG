# Generated by Django 4.2.6 on 2023-10-27 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dictec', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dictamenfinal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Titulo', models.CharField(max_length=200)),
                ('IDuser', models.CharField(max_length=20)),
                ('Nombre', models.CharField(max_length=80)),
                ('Oficina', models.CharField(max_length=80)),
                ('Direccion', models.CharField(max_length=80)),
                ('Tipo_Equipo', models.CharField(max_length=80)),
                ('Marca', models.CharField(max_length=80)),
                ('Modelo', models.CharField(max_length=80)),
                ('Num_Serie', models.CharField(max_length=80)),
                ('Caracteristicas', models.CharField(max_length=200)),
                ('Problema', models.TextField(max_length=1000)),
                ('Analisis', models.TextField(max_length=1000)),
                ('Proceso_Realizado', models.TextField(max_length=1000)),
                ('Dictamen_Final', models.TextField(max_length=1000)),
                ('Creacion', models.DateTimeField(auto_now_add=True)),
                ('Datecompleted', models.DateTimeField(blank=True, null=True)),
                ('Pendiente', models.BooleanField(default=False)),
                ('Imprimir', models.BooleanField(default=False)),
                ('Creado', models.BooleanField(default=False)),
                ('Finalizado', models.BooleanField(default=False)),
            ],
        ),
    ]
