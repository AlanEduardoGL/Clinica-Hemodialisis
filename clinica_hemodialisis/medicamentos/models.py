from django.db import models

# Create your models here.


class Medicine(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre")
    description = models.TextField(verbose_name="Descripcion")
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Precio")
    stock = models.PositiveIntegerField(verbose_name="Stock")
    expiration_date = models.DateField(verbose_name="Fecha de expiracion")
    category = models.CharField(max_length=100, verbose_name="Categoria")
    brand = models.CharField(max_length=100, verbose_name="Marca")
    supplier = models.CharField(max_length=100, verbose_name="Proveedor")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de Actualizacion")

     # Agregamos meta datos extendidos.
    class Meta:
        verbose_name = "medicamento"
        verbose_name_plural = "medicamentos"
        ordering = ["-created"] # Campo de ordenamiento par nuestros registros. Del mas nuevo al mas antiguo.

    # Devolvemos el "name" del medicamento.
    def __str__(self):
        return self.name