from django import forms
from django.utils import timezone

from .models import Trip


class TripForm(forms.ModelForm):

    class Meta:
        model = Trip

        fields = [
            'vehicle',
            'driver',
            'origin',
            'destination',
            'departure_date',
            'arrival_date',
            'initial_mileage',
            'final_mileage',
            'status',
            'observations',
        ]

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        self.fields['vehicle'].queryset = (
            self.fields['vehicle'].queryset.filter(
                status='active'
            )
        )

        self.fields['driver'].queryset = (
            self.fields['driver'].queryset.filter(
                status='active',
                license_expiry__gte=timezone.now().date()
            )
        )

    def clean_final_mileage(self):

        final_mileage = self.cleaned_data['final_mileage']
        initial_mileage = self.cleaned_data.get('initial_mileage')

        if (
            final_mileage is not None
            and initial_mileage is not None
            and final_mileage < initial_mileage
        ):

            raise forms.ValidationError(
                'El kilometraje final no puede ser menor al kilometraje inicial.'
            )

        return final_mileage

    def clean(self):

        cleaned_data = super().clean()

        departure_date = cleaned_data.get(
            'departure_date'
        )

        arrival_date = cleaned_data.get(
            'arrival_date'
        )

        if (
            departure_date
            and arrival_date
            and arrival_date < departure_date
        ):

            raise forms.ValidationError(
                'La fecha de llegada no puede ser anterior a la fecha de salida.'
            )

        return cleaned_data