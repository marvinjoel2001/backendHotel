from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    email = models.EmailField()
    ci = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre


class Habitacion(models.Model):
    numero = models.IntegerField(unique=True)
    capacidad = models.IntegerField(validators=[MinValueValidator(1)])
    ocupada = models.BooleanField(default=False)
    precio = models.DecimalField(max_digits=8, decimal_places=2, validators=[MinValueValidator(0.01)])

    def __str__(self):
        return f'Habitación {self.numero}'


class Pago(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='pagos')
    habitacion = models.ForeignKey(Habitacion, on_delete=models.CASCADE, related_name='pagos')
    fecha_entrada = models.DateField()
    fecha_salida = models.DateField()
    monto = models.DecimalField(max_digits=8, decimal_places=2, validators=[MinValueValidator(0.01)])
    fecha = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'Habitación {self.habitacion}'


class Reserva(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    habitacion = models.ForeignKey(Habitacion, on_delete=models.CASCADE)
    fecha_entrada = models.DateField()
    fecha_salida = models.DateField()

    def __str__(self):
        return f'Reserva de {self.cliente} - Habitación {self.habitacion}'
