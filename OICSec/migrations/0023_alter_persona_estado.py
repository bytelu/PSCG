# Generated by Django 5.0.4 on 2024-07-16 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OICSec', '0022_alter_persona_estado_alter_persona_sexo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='estado',
            field=models.IntegerField(blank=True, choices=[(0, 'Inactivo'), (1, 'Activo')], default=1, null=True),
        ),
    ]
