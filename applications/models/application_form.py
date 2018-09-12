from django.contrib.auth.models import User
from django.db import models
from django.forms.widgets import HiddenInput


class ApplicationForm(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    mailing_address = models.CharField(max_length=100)
