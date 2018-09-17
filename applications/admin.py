from django.contrib import admin
from .models.application_form import ApplicationFormModel
from django.contrib.auth.models import User



@admin.register(ApplicationFormModel)
class ApplicationFormModelAdmin(admin.ModelAdmin):

    def first_name(self, instance):
        return instance.user.first_name

    def last_name(self, instance):
        return instance.user.last_name

    list_display = ('user', 'first_name', 'last_name', 'mailing_address',)


# class ApplicationInLine(admin.TabularInline):
#     model = ApplicationFormModel
#     fields = ('first_name',)

# class UserInLine(admin.TabularInline):
#         inlines = [
#         ApplicationInLine,
#     ]

# @admin.register(ApplicationFormModel)
# class ApplicationFormModelAdmin(admin.ModelAdmin):

#     list_display = ('user', 'mailing_address',)

