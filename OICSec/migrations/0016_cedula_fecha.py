# Generated by Django 5.0.4 on 2024-07-08 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OICSec', '0015_cedulaauditoria_cedulacontrolinterno_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cedula',
            name='fecha',
            field=models.DateField(blank=True, null=True),
        ),
    ]
