from django.db import models

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre


class Instrumento(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT, related_name='instrumentos')
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    precio = models.DecimalField(max_digits=10, decimal_places=0)
    fecha_ingreso = models.DateField()
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre
