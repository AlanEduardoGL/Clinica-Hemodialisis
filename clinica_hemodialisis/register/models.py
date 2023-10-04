from django.db import models

# Create your models here.

class User(models.Model):
    id_user = models.AutoField(primary_key=True, verbose_name="ID del Usuario")
    username = models.CharField(max_length=255, verbose_name="Nombre de Usuario")
    name = models.CharField(max_length=255, verbose_name="Nombre")
    last_name = models.CharField(max_length=255, verbose_name="Apellido")
    age = models.IntegerField(verbose_name="Edad")
    cell_number = models.CharField(unique=True, max_length=10, verbose_name="Telefono Celular")
    email = models.EmailField(unique=True, verbose_name="Correo Electronico")
    password = models.CharField(max_length=130)
    administrator_profile = models.BooleanField(default=False, verbose_name="Perfil Administrador")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de Actualizacion")

    # Agregamos meta datos extendidos.
    class Meta:
        verbose_name = "usuario"
        verbose_name_plural = "usuarios"
        ordering = ["-created"] # Campo de ordenamiento par nuestros registros. Del mas nuevo al mas antiguo.

    # Devolvemos el nombre del proyecto.
    def __str__(self):
        return self.nombre