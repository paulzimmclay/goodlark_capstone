from django import forms

class ApplicationForm(forms.ModelForm):
    
    class Meta:
        model = ApplicationForm
        fields = '__all__'