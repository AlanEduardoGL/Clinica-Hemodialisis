from django.db import models
from django.contrib.auth.models import AbstractUser
from register.models import User

# Create your models here.


class Patient(AbstractUser):
    id_patient = models.AutoField(primary_key=True, verbose_name="ID Paciente")
    id_username = models.ForeignKey(User, on_delete=models.CASCADE)
    patient_name = models.CharField(max_length=255, verbose_name="Nombre Paciente")
    patient_last_name = models.CharField(max_length=255, verbose_name="Apellido Paciente")
    patient_age = models.IntegerField(verbose_name="Edad")
    gender_choices = [
    ('M', 'Masculino'),
    ('F', 'Femenino'),
    ('O', 'Otro'),
    ]
    gender = models.CharField(max_length=1, choices=gender_choices, verbose_name="Género")
    cell_number = models.CharField(unique=True, max_length=10, verbose_name="Telefono Celular")
    email = models.EmailField(unique=True, verbose_name="Correo Electronico")
    allergies = models.TextField(max_length=500, verbose_name="Alergias")
    symptoms = models.TextField(max_length=500, verbose_name="Síntomas")
    street_address = models.CharField(max_length=255, verbose_name="Dirección")
    city = models.CharField(max_length=255, verbose_name="Ciudad")
    state = models.CharField(max_length=255, verbose_name="Estado")
    postal_code = models.CharField(max_length=10, verbose_name="Código Postal")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de Actualizacion")

    groups = models.ManyToManyField(
        "auth.Group",
        blank=True,
        related_name="patients_group"  # Cambia esto a un nombre que prefieras
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission",
        blank=True,
        related_name="patients_permissions"  # Cambia esto a un nombre que prefieras
    )

    # Agregamos meta datos extendidos.
    class Meta:
        verbose_name = "paciente"
        verbose_name_plural = "pacientes"
        ordering = ["-created"] # Campo de ordenamiento par nuestros registros. Del mas nuevo al mas antiguo.

    # Devolvemos el nombre del paciente.
    def __str__(self):
        return self.patient_name