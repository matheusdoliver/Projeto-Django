# Generated by Django 5.0.3 on 2024-03-20 18:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0002_rename_nots_computador'),
    ]

    operations = [
        migrations.AddField(
            model_name='computador',
            name='data_entrada',
            field=models.DateTimeField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='computador',
            name='nome',
            field=models.CharField(max_length=35),
        ),
    ]