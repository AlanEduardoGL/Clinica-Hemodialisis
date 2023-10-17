from django.db import models
from medicamentos.models import Medicine
from pacientes.models import Patient
from register.models import User

# Create your models here.


class Quotes(models.Model):
    medic = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Medico Asignado")
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, verbose_name="Paciente")
    date = models.DateField(verbose_name="Fecha Cita")
    symptoms = models.TextField(verbose_name="Sintomas")
    medicines = models.ManyToManyField(Medicine, verbose_name="Medicamentos")
    total_price = models.FloatField(verbose_name="Precio Total")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de Actualizacion")

    # Agregamos meta datos extendidos.
    class Meta:
        verbose_name = "cita"
        verbose_name_plural = "citas"
        # Campo de ordenamiento par nuestros registros. Del mas nuevo al mas antiguo.
        ordering = ["-created"]

    # Devolvemos el nombre del medico.
    def __str__(self):
        return self.medic
