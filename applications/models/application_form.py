from django.contrib.auth.models import User
from django.db import models

from multiselectfield import MultiSelectField

# ...

MY_CHOICES = (('item_key1', 'Item title 1.1'),
              ('item_key2', 'Item title 1.2'),
              ('item_key3', 'Item title 1.3'),
              ('item_key4', 'Item title 1.4'),
              ('item_key5', 'Item title 1.5'))


class ApplicationFormModel(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    my_field = MultiSelectField(blank=True, choices=MY_CHOICES)
    mailing_address = models.CharField(blank=True, max_length=100)
    city = models.CharField(blank=True, max_length=100)
    