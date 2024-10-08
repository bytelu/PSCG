# Generated by Django 5.0.4 on 2024-07-02 18:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OICSec', '0011_remove_intervencion_rubro_alter_intervencion_alcance_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='TipoCedula',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('tipo', models.CharField(blank=True, max_length=200, null=True)),
            ],
            options={
                'db_table': 'tipo_cedula',
            },
        ),
        migrations.AddField(
            model_name='cedula',
            name='id_archivo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='OICSec.archivo'),
        ),
        migrations.AddField(
            model_name='cedula',
            name='id_tipo_cedula',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='OICSec.tipocedula'),
        ),
    ]
