from django.db import models
from twilio.rest import Client

# Create your models here.


class Transaction(models.Model):
    value = models.PositiveIntegerField()
    from_user = models.CharField(max_length=256, blank=True, null=True, default='')

    def __str__(self):
        return str(self.value)

    # save method
    def save(self, *args, **kwargs):
        # if test_result is less than 80 execute this
        if self.value < 80:
            # twilio code
            account_sid = 'AC9836993aec5aa086a75a41350bb8ce6e'
            auth_token = 'f6aff965fafb23eedc813aec1613cb43'
            client = Client(account_sid, auth_token)

            message = client.messages.create(
                body=f'Value: {self.value}',
                from_='+16064044957',
                to='+5491132896065'
            )

            print(message.sid)
        return super().save(*args, **kwargs)
