from django import forms
from django.utils import timezone

from .models import Expense


class ExpenseForm(forms.ModelForm):

    class Meta:

        model = Expense

        fields = [
            'vehicle',
            'trip',
            'expense_type',
            'date',
            'amount',
            'description',
            'observations',
        ]


    def clean_description(self):
        description = self.cleaned_data.get('description')

        if description:
            return description.strip()

        return description


    def clean_observations(self):
        observations = self.cleaned_data.get('observations')

        if observations:
            return observations.strip()

        return observations


    def clean_amount(self):
        amount = self.cleaned_data.get('amount')

        if amount < 0:
            raise forms.ValidationError(
                'El monto del gasto no puede ser negativo.'
            )

        return amount


    def clean(self):

        cleaned_data = super().clean()

        expense_type = cleaned_data.get(
            'expense_type'
        )

        trip = cleaned_data.get(
            'trip'
        )

        date = cleaned_data.get(
            'date'
        )


        if date and date > timezone.now().date():

            raise forms.ValidationError(
                'La fecha del gasto no puede ser futura.'
            )


        if expense_type == 'fuel' and not trip:

            raise forms.ValidationError(
                'Un gasto de combustible debe estar asociado a un viaje.'
            )


        return cleaned_data