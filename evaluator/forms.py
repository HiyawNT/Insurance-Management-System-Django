from django import forms
from django.contrib.auth.models import User
from . import models
from manager import models as CMODEL






class EvaluatorUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','email','password']
        widgets = {
        'password': forms.PasswordInput()
        }

class EvaluatorForm(forms.ModelForm):
    class Meta:
        model=models.Evaluator
        fields=['address','mobile','profile_pic']