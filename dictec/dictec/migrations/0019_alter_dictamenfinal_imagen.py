# Generated by Django 4.2.6 on 2023-12-07 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dictec', '0018_alter_dictamenfinal_revisionjefe'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dictamenfinal',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='static/img'),
        ),
    ]
