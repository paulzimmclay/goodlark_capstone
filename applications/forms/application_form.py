from django import forms
from applications.models import *

class ApplicationForm(forms.ModelForm):
    
    class Meta:
        model = ApplicationFormModel
        fields = '__all__'