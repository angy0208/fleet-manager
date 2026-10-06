from django.db import models

from vehicles.models import Vehicle
from trips.models import Trip


class Expense(models.Model):

    EXPENSE_TYPES = [
        ('fuel', 'Combustible'),
        ('toll', 'Peaje'),
        ('allowance', 'Viático'),
        ('washing', 'Lavado'),
        ('insurance', 'Seguro'),
        ('other', 'Otro'),
    ]


    vehicle = models.ForeignKey(
        Vehicle,
        on_delete=models.CASCADE
    )

    trip = models.ForeignKey(
        Trip,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    expense_type = models.CharField(
        max_length=20,
        choices=EXPENSE_TYPES
    )

    date = models.DateField()

    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    description = models.TextField()

    observations = models.TextField(
        blank=True,
        null=True
    )


    class Meta:
        db_table = 'expenses'


    def __str__(self):

        return f"{self.vehicle} - {self.get_expense_type_display()}"