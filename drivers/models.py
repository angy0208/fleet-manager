from django.db import models


class Driver(models.Model):

    STATUS_CHOICES = [
        ('active', 'Activo'),
        ('inactive', 'Inactivo'),
        ('suspended', 'Suspendido'),
    ]

    first_name = models.CharField(
        max_length=50
    )

    last_name = models.CharField(
        max_length=50
    )

    identification = models.CharField(
        max_length=20,
        unique=True
    )

    phone = models.CharField(
        max_length=20,
        blank=True,
        null=True
    )

    address = models.CharField(
        max_length=200,
        blank=True,
        null=True
    )

    birth_date = models.DateField(
        blank=True,
        null=True
    )

    license_number = models.CharField(
        max_length=30,
        unique=True
    )

    license_type = models.CharField(
        max_length=30
    )

    license_expiry = models.DateField()

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='active'
    )

    hire_date = models.DateField(
        blank=True,
        null=True
    )

    class Meta:
        db_table = 'drivers'

    def __str__(self):
        return f"{self.first_name} {self.last_name}"