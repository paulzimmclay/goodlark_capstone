from django import forms
from applications.models import *

class ApplicationForm(forms.ModelForm):
    
    class Meta:
        model = ApplicationForm
        fields = '__all__'