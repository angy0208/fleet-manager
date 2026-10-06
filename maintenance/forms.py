from django import forms
from django.utils import timezone

from .models import Maintenance


class MaintenanceForm(forms.ModelForm):

    class Meta:
        model = Maintenance
        fields = [
            'vehicle',
            'maintenance_type',
            'category',
            'date',
            'mileage',
            'cost',
            'status',
            'description',
            'observations',
        ]

    def clean_cost(self):

        cost = self.cleaned_data['cost']

        if cost < 0:
            raise forms.ValidationError(
                'El costo del mantenimiento no puede ser negativo.'
            )

        return cost

    def clean(self):

        cleaned_data = super().clean()

        vehicle = cleaned_data.get('vehicle')
        date = cleaned_data.get('date')
        mileage = cleaned_data.get('mileage')
        status = cleaned_data.get('status')

        if (
            date
            and status == 'completed'
            and date > timezone.now().date()
        ):
            raise forms.ValidationError(
                'Un mantenimiento completado no puede tener una fecha futura.'
            )

        if (
            vehicle
            and mileage is not None
            and mileage > vehicle.current_mileage
        ):
            raise forms.ValidationError(
                'El kilometraje del mantenimiento no puede ser mayor al kilometraje actual del vehículo.'
            )

        return cleaned_data

    def clean_description(self):

        description = self.cleaned_data['description']

        return description.strip()

    def clean_observations(self):

        observations = self.cleaned_data['observations']

        if observations:
            return observations.strip()

        return observations