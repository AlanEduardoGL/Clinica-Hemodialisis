# Generated by Django 4.2.5 on 2023-09-21 23:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id_usuario', models.AutoField(primary_key=True, serialize=False, verbose_name='ID Usuario')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombres de Usuario')),
                ('apellido_paterno', models.CharField(max_length=100, verbose_name='Apellido Paterno del Usuario')),
                ('apellido_materno', models.CharField(max_length=100, verbose_name='Apellido Materno del Usuario')),
                ('edad', models.IntegerField(verbose_name='Edad')),
                ('especialidad', models.CharField(max_length=100, verbose_name='Especialidad')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de actualizacion')),
            ],
            options={
                'verbose_name': 'usuario',
                'verbose_name_plural': 'usuarios',
                'ordering': ['-created'],
            },
        ),
    ]
