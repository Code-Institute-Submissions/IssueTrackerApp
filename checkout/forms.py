"""Form for checkout"""
from django import forms

class MakePaymentForm(forms.Form):
    """Form for making payments"""

    MONTH_CHOICES = [(i, i) for i in range(1, 13)]
    YEAR_CHOICES = [(i, i) for i in range(2018, 2037)]

    credit_card_number = forms.CharField(label='Credit card number', required=False)
    expiry_month = forms.ChoiceField(label='Month', choices=MONTH_CHOICES, required=False)
    expiry_year = forms.ChoiceField(label='Year', choices=YEAR_CHOICES, required=False)
    cvc = forms.CharField(label='Security code (CVC)', required=False)
    stripe_id = forms.CharField(widget=forms.HiddenInput)
