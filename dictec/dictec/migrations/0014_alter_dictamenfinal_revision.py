# Generated by Django 4.2.6 on 2023-12-07 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dictec', '0013_alter_dictamenfinal_revision'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dictamenfinal',
            name='Revision',
            field=models.IntegerField(blank=True, choices=[(1, 'Corregido'), (2, 'Corregido 2'), (3, 'Corregido 3'), (4, 'Modificado')]),
        ),
    ]
