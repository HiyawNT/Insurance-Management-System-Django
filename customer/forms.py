from django import forms
from django.contrib.auth.models import User
from . import models
from manager import models as CMODEL


class CustomerUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','email','password']
        widgets = {
        'password': forms.PasswordInput()
        }

class CustomerForm(forms.ModelForm):
    class Meta:
        model=models.Customer
        fields=['address','mobile','profile_pic']

class PolicyForm(forms.ModelForm):
    vehicle_policy = forms.ModelChoiceField(queryset=CMODEL.Category.objects.all(),empty_label="Category Name", to_field_name="id")
    class Meta:
        model=CMODEL.vehicle_policy
        fields=['proposer_name','father_name',
                'age','address', 'profession',
                'phone_no','policychoice', 'pobox', 'licenceno',
                'durationfrom', 'durationto', 'plateno',
                'vehiclename', 'vehiclemodel', 'yearofmanufacture',
                'yearofpurchase', 'priceofcar', 
                ]

class ClaimForm(forms.ModelForm):
    vehicle_policy = forms.ModelChoiceField(queryset=CMODEL.Category.objects.all(),empty_label="Category Name", to_field_name="id")
    class Meta:
        model=CMODEL.claim_form
        fields=['insured_name','phone_no',
                'address', 'profession',
                'policy_number','renewal_date', 'vehiclemodel', 'yearofmanufacture',
                'plateno', 'licenceno', 'vehicle_purpose',
                'horsepower', 'carrying_capacity', 'driver_name',
                'driver_age', 'driver_phone_no','licence_expiry_date',  'driver_address',
                'licence_number', 'driver_profession',
                'licence_grade', 'accident_proof','accident_date','accident_place','accident_time','accident_description',
                ]
        widgets = {
        'accident_description': forms.Textarea(attrs={'rows': 10, 'cols': 100})
        }