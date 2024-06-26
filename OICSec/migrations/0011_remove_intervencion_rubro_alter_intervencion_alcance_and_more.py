# Generated by Django 5.0.4 on 2024-06-26 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OICSec', '0010_remove_intervencion_rubro_intervencion_alcance_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='intervencion',
            name='rubro',
        ),
        migrations.AlterField(
            model_name='intervencion',
            name='alcance',
            field=models.TextField(blank=True, max_length=5000, null=True),
        ),
        migrations.AlterField(
            model_name='intervencion',
            name='antecedentes',
            field=models.TextField(blank=True, max_length=5000, null=True),
        ),
        migrations.AlterField(
            model_name='intervencion',
            name='denominacion',
            field=models.TextField(blank=True, max_length=5000, null=True),
        ),
        migrations.AlterField(
            model_name='intervencion',
            name='objetivo',
            field=models.TextField(blank=True, max_length=5000, null=True),
        ),
        migrations.AlterField(
            model_name='intervencion',
            name='unidad',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
    ]
