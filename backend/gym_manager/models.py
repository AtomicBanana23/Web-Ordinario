from django.db import models

# Create your models here.
class empleado(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    rol = models.CharField(max_length=50)
    activo = models.BooleanField(default=True)

class cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    tipo_membresia = models.CharField(max_length=50)
    activo = models.BooleanField(default=True)
    fecha_prox_pago = models.DateField()
    entrenador_id = models.ForeignKey(empleado, on_delete=models.CASCADE)

class maquina(models.Model):
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=50)
    estado = models.CharField(max_length=50, choices=[('disponible', 'Disponible'), ('en_mantenimiento', 'En Mantenimiento')])

class producto(models.Model):
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()