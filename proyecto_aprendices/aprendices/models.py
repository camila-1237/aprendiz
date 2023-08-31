from django.db import models

class Aprendiz(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    numero_documento = models.CharField(max_length=20)
    tipo_documento = models.CharField(max_length=20)
    numero_ficha = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

