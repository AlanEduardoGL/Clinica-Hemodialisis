# Generated by Django 4.2.5 on 2023-10-10 16:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pacientes', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='username',
        ),
    ]
