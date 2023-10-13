# Generated by Django 4.2.5 on 2023-10-13 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Medicine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nombre')),
                ('description', models.TextField(verbose_name='Descripcion')),
                ('price', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Precio')),
                ('stock', models.PositiveIntegerField(verbose_name='Stock')),
                ('expiration_date', models.DateField(verbose_name='Fecha de expiracion')),
                ('category', models.CharField(max_length=50, verbose_name='Categoria')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creacion')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de Actualizacion')),
            ],
            options={
                'verbose_name': 'medicamento',
                'verbose_name_plural': 'medicamentos',
                'ordering': ['-created'],
            },
        ),
    ]
