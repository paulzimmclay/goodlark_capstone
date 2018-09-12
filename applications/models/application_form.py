from django.contrib.auth.models import User
from django.db import models


class ApplicationForm(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mailing_address = models.CharField(max_length=100)