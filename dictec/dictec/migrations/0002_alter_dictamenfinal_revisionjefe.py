# Generated by Django 4.2.6 on 2023-12-19 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dictec', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dictamenfinal',
            name='Revisionjefe',
            field=models.CharField(blank=True, choices=[('Pendiente', 'Pendiente'), ('Pendiente 2', 'Pendiente 2'), ('Pendiente 3', 'Pendiente 3'), ('Aprobado', 'Aprobado')], max_length=80),
        ),
    ]
