# Generated by Django 5.0.4 on 2024-06-25 19:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('OICSec', '0008_alter_tiporevision_clave_alter_tiporevision_tipo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='controlinterno',
            old_name='id_sector_revision',
            new_name='id_programa_revision',
        ),
    ]
