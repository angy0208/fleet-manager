from django import forms
from django.utils import timezone

from .models import Vehicle


class VehicleForm(forms.ModelForm):

    class Meta:
        model = Vehicle
        fields = [
            'plate',
            'internal_number',
            'brand',
            'model',
            'year',
            'vehicle_type',
            'status',
            'current_mileage',
        ]

    def clean_year(self):

        year = self.cleaned_data['year']
        current_year = timezone.now().year

        if year < 1900:
            raise forms.ValidationError(
                'El año del vehículo no puede ser anterior a 1900.'
            )

        if year > current_year + 1:
            raise forms.ValidationError(
                'El año del vehículo no puede ser posterior al año siguiente.'
            )

        return year

    def clean_current_mileage(self):

        current_mileage = self.cleaned_data['current_mileage']

        if self.instance.pk:

            if current_mileage < self.instance.current_mileage:

                raise forms.ValidationError(
                    'El kilometraje no puede ser menor al kilometraje actual del vehículo.'
                )

        return current_mileage

    def clean(self):

        cleaned_data = super().clean()

        text_fields = [
            'plate',
            'internal_number',
            'brand',
            'model',
        ]

        for field in text_fields:

            value = cleaned_data.get(field)

            if value:
                cleaned_data[field] = value.strip()

        return cleaned_data