# Generated by Django 5.0.4 on 2024-06-26 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OICSec', '0009_rename_id_sector_revision_controlinterno_id_programa_revision'),
    ]

    operations = [
        migrations.AddField(
            model_name='intervencion',
            name='alcance',
            field=models.CharField(blank=True, max_length=5000, null=True),
        ),
        migrations.AddField(
            model_name='intervencion',
            name='antecedentes',
            field=models.CharField(blank=True, max_length=5000, null=True),
        ),
        migrations.AddField(
            model_name='intervencion',
            name='fuerza_auditores',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='intervencion',
            name='fuerza_responsables',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='intervencion',
            name='fuerza_supervision',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='intervencion',
            name='inicio',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='intervencion',
            name='objetivo',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='intervencion',
            name='termino',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='intervencion',
            name='denominacion',
            field=models.CharField(blank=True, max_length=5000, null=True),
        ),
    ]
