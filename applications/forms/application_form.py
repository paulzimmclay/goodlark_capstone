from django import forms
from applications.models import *

class ApplicationForm(forms.ModelForm):
    
    class Meta:
        model = ApplicationFormModel
        exclude = ['user']
        widgets = {
            'assistance_for': forms.RadioSelect(),
            'already_accumulated_debt': forms.RadioSelect(),
            'previously_received_goodlark': forms.RadioSelect(),
            'family_received_scholarship': forms.RadioSelect(),
        }