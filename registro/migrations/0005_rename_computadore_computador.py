# Generated by Django 5.0.3 on 2024-03-20 18:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0004_computadore_delete_computador'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='computadore',
            new_name='computador',
        ),
    ]