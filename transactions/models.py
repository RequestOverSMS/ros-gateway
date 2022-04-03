from django.db import models
from twilio.rest import Client

# Create your models here.


class Transaction(models.Model):
    value = models.PositiveIntegerField()
    from_user = models.CharField(max_length=256, blank=True, null=True, default='')

    def __str__(self):
        return str(self.value)

