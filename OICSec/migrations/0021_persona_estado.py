# Generated by Django 5.0.4 on 2024-07-16 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OICSec', '0020_remove_cedulacontrolinterno_id_cedula_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='persona',
            name='estado',
            field=models.IntegerField(blank=True, max_length=1, null=True),
        ),
    ]
