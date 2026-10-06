from django.db import models

from vehicles.models import Vehicle


class Maintenance(models.Model):

    MAINTENANCE_TYPE_CHOICES = [
        ('oil_change', 'Cambio de aceite'),
        ('tires', 'Cambio de neumáticos'),
        ('brakes', 'Revisión de frenos'),
        ('engine', 'Revisión del motor'),
        ('electrical', 'Sistema eléctrico'),
        ('cooling', 'Sistema de refrigeración'),
        ('transmission', 'Transmisión'),
        ('other', 'Otro'),
    ]

    CATEGORY_CHOICES = [
        ('preventive', 'Preventivo'),
        ('corrective', 'Correctivo'),
    ]

    STATUS_CHOICES = [
        ('scheduled', 'Programado'),
        ('in_progress', 'En proceso'),
        ('completed', 'Completado'),
        ('cancelled', 'Cancelado'),
    ]

    vehicle = models.ForeignKey(
        Vehicle,
        on_delete=models.PROTECT
    )

    maintenance_type = models.CharField(
        max_length=30,
        choices=MAINTENANCE_TYPE_CHOICES
    )

    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES
    )

    date = models.DateField()

    mileage = models.PositiveIntegerField()

    cost = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='scheduled'
    )

    description = models.TextField()

    observations = models.TextField(
        blank=True,
        null=True
    )

    class Meta:
        db_table = 'maintenance'
        ordering = ['-date']

    def __str__(self):
        return (
            f"{self.vehicle} - "
            f"{self.get_maintenance_type_display()}"
        )