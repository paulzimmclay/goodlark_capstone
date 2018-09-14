from django import forms
from applications.models import *

class ApplicationForm(forms.ModelForm):
    
    class Meta:
        model = ApplicationFormModel
        exclude = ['user']
        widgets = {
            'assistance_for': forms.RadioSelect(),
        }