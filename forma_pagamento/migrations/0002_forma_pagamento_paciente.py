# Generated by Django 4.0.2 on 2022-02-09 01:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('paciente', '0001_initial'),
        ('forma_pagamento', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='forma_pagamento',
            name='paciente',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='paciente.paciente'),
            preserve_default=False,
        ),
    ]
