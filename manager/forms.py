from django import forms
from django.contrib.auth.models import User
from . import models

# class ContactusForm(forms.Form):
#     Name = forms.CharField(max_length=30)
#     Subject = forms.CharField(max_length=70)
#     Email = forms.EmailField()
#     Message = forms.CharField(max_length=500,widget=forms.Textarea(attrs={'rows': 3, 'cols': 30}))

class ContactusForm(forms.ModelForm):
    class Meta:
        model = models.Contactus
        fields = ['Name','Email', 'Subject', 'Message']
        widgets={
            'Message' : forms.Textarea(attrs={'rows': 6, 'cols': 30})
        }


class CategoryForm(forms.ModelForm):
    class Meta:
        model=models.Category
        fields=['category_name']

class PolicyForm(forms.ModelForm):
    category=forms.ModelChoiceField(queryset=models.Category.objects.all(),empty_label="Category Name", to_field_name="id")
    class Meta:
        model=models.Policy
        fields=['policy_name','sum_assurance','premium','tenure']
        
class AddClaimForm(forms.ModelForm):
    class Meta:
        model=models.AddClaim
        category=forms.ModelChoiceField(queryset=models.Category.objects.all(),empty_label="Category Name", to_field_name="id")
        
        fields=['category','claim_name']

class QuestionForm(forms.ModelForm):
    class Meta:
        model=models.Question
        fields=['description']
        widgets = {
        'description': forms.Textarea(attrs={'rows': 6, 'cols': 30})
        }

class vehiclepolicy(forms.ModelForm):
    vehicle_policy = forms.ModelChoiceField(queryset=models.Category.objects.all(),empty_label="Category Name", to_field_name="id")
    class Meta:
        model=models.vehicle_policy
        fields=['vehicle_policy','proposer_name','father_name',
                'age','address', 'profession',
                'phone_no', 'pobox', 'licenceno',
                'durationfrom', 'durationto', 'plateno',
                'vehiclename', 'vehiclemodel', 'yearofmanufacture',
                'yearofpurchase', 'priceofcar', 
                ]