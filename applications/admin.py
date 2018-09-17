from django.contrib import admin
from .models.application_form import ApplicationFormModel

# admin.site.register(ApplicationFormModel)

@admin.register(ApplicationFormModel)
class ApplicationFormModelAdmin(admin.ModelAdmin):
    list_display = ('user', 'mailing_address')