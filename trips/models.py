from django.db import models
from vehicles.models import Vehicle
from drivers.models import Driver

class Trip(models.Model):
    STATUS_CHOICES = [
        ('scheduled', 'Programado'),
        ('in_progress', 'En curso'),
        ('completed', 'Completado'),
        ('cancelled', 'Cancelado'),
    ]

    vehicle = models.ForeignKey(Vehicle, on_delete=models.PROTECT)
    driver = models.ForeignKey(Driver, on_delete=models.PROTECT)
    origin = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    departure_date = models.DateTimeField()
    arrival_date = models.DateTimeField(blank=True, null=True)
    initial_mileage = models.PositiveIntegerField()
    final_mileage = models.PositiveIntegerField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='scheduled')
    observations = models.TextField(blank=True, null=True)
    class Meta:
        db_table = 'trips'

    def __str__(self):
        return f"{self.origin} -> {self.destination}"

