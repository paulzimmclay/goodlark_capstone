from django.contrib import admin
from .models.application_form import ApplicationFormModel
from django.contrib.auth.models import User
from actions import export_as_csv_action

@admin.register(ApplicationFormModel)
class ApplicationFormModelAdmin(admin.ModelAdmin):
	
    actions = [export_as_csv_action("CSV Export")]
    
    list_display = ('user',)