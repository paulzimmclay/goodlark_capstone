from django.db import models

class ApplicationForm(models.Model):
    MailingAddress = models.CharField(default="", max_length=100)