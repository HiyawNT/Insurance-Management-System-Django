from django import forms
from django.contrib.auth.models import User
from . import models




class PaymentForm(forms.ModelForm):
    bank_name=forms.ModelChoiceField(queryset=models.BankNameLists.objects.all(),empty_label="Bank Name", to_field_name="id")
    payment_type = forms.ModelChoiceField(queryset=models.Category.objects.all(),empty_label="payment type", to_field_name="id")
    class Meta:
        model=models.Payment
        fields=['account_no','bank_name','payment_amount', 'transaction_id', 'payment_proof']