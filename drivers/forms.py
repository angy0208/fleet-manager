from django import forms
from django.utils import timezone

from .models import Driver


class DriverForm(forms.ModelForm):

    class Meta:
        model = Driver
        fields = [
            'first_name',
            'last_name',
            'identification',
            'phone',
            'address',
            'birth_date',
            'license_number',
            'license_type',
            'license_expiry',
            'status',
            'hire_date',
        ]

    def clean_birth_date(self):

        birth_date = self.cleaned_data['birth_date']

        if birth_date:

            if birth_date > timezone.now().date():

                raise forms.ValidationError(
                    'La fecha de nacimiento no puede ser futura.'
                )

        return birth_date

    def clean_hire_date(self):

        hire_date = self.cleaned_data['hire_date']

        if hire_date:

            if hire_date > timezone.now().date():

                raise forms.ValidationError(
                    'La fecha de ingreso no puede ser futura.'
                )

        return hire_date

    def clean_license_expiry(self):

        license_expiry = self.cleaned_data['license_expiry']

        if license_expiry < timezone.now().date():

            raise forms.ValidationError(
                'La licencia del conductor está vencida.'
            )

        return license_expiry

    def clean(self):

        cleaned_data = super().clean()

        text_fields = [
            'first_name',
            'last_name',
            'identification',
            'phone',
            'address',
            'license_number',
            'license_type',
        ]

        for field in text_fields:

            value = cleaned_data.get(field)

            if value:

                cleaned_data[field] = value.strip()

        return cleaned_data