from django.db import models


# Create your models here.
class Persona(models.Model):
    nombre = models.CharField(max_length=10)
    apellido = models.CharField(max_length=10)
    fecha_de_nacimiento = models.DateField()

    def __str__(self):
        return f" ID: {self.id} Nombre:{self.nombre}, Apellido:{self.apellido}, Fecha Nacimiento: {self.fecha_de_nacimiento}"



class Inventario (models.Model):
    Producto = models.CharField(max_length=200)
    Cantidad = models.IntegerField()

    def _str_(self):
        return f"ID: {self.id} Producto: {self.Producto}- Cantidad: {self.Cantidad }"

    