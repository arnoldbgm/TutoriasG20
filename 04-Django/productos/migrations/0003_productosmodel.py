# Generated by Django 5.1.2 on 2024-10-21 02:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0002_alter_categoriasmodel_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductosModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stock', models.IntegerField()),
                ('titulo', models.CharField(max_length=255)),
                ('contenido', models.TextField(blank=True)),
                ('categoria_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productos.categoriasmodel')),
            ],
            options={
                'db_table': 'productos',
            },
        ),
    ]