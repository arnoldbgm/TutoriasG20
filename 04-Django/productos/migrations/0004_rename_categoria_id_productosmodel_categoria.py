# Generated by Django 5.1.2 on 2024-10-21 02:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0003_productosmodel'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productosmodel',
            old_name='categoria_id',
            new_name='categoria',
        ),
    ]
