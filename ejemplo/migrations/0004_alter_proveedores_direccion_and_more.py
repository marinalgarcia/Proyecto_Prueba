# Generated by Django 4.1.2 on 2022-10-28 01:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ejemplo', '0003_proveedores'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proveedores',
            name='direccion',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='proveedores',
            name='empresa',
            field=models.CharField(max_length=100),
        ),
    ]
