# Generated by Django 5.0.4 on 2024-06-25 17:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('OICSec', '0004_alter_sectorrevision_tipo'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='SectorRevision',
            new_name='ProgramaRevision',
        ),
        migrations.AlterModelTable(
            name='programarevision',
            table='programa_revision',
        ),
    ]
