from django.contrib.auth.models import User
from django.db import models


class ApplicationFormModel(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    mailing_address = models.CharField(blank=True, max_length=100)
