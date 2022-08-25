from django.db import models

# Create your models here.

class Marca(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()
    descripción = models.TextField()
    nuevo = models.BooleanField()
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT)
    fecha_fabricación = models.DateField()

    def __str__(self):
        return self.nombre

class Mesas(models.Model):
    nombre = models.CharField(max_length=10)
    activo = models.BooleanField()

    def __str__(self):
        return self.nombre
