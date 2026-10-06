from django.db import models


class Vehicle(models.Model):

    VEHICLE_TYPE_CHOICES = [
        ('truck', 'Camión'),
        ('pickup', 'Camioneta'),
        ('tractor', 'Tracto'),
        ('trailer', 'Remolque'),
        ('other', 'Otro'),
    ]

    STATUS_CHOICES = [
        ('active', 'Activo'),
        ('maintenance', 'En mantenimiento'),
        ('out_of_service', 'Fuera de servicio'),
    ]

    plate = models.CharField(
        max_length=20,
        unique=True
    )

    internal_number = models.CharField(
        max_length=20,
        unique=True,
        blank=True,
        null=True
    )

    brand = models.CharField(
        max_length=50
    )

    model = models.CharField(
        max_length=50
    )

    year = models.PositiveIntegerField()

    vehicle_type = models.CharField(
        max_length=20,
        choices=VEHICLE_TYPE_CHOICES,
        default='truck'
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='active'
    )

    current_mileage = models.PositiveIntegerField(
        default=0
    )

    class Meta:
        db_table = 'vehicles'

    def __str__(self):
        return f"{self.brand} {self.model} - {self.plate}"