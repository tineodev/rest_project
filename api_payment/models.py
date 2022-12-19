from django.db import models

from django.contrib.auth.models import User
from api_services.models import Services

# Create your models here.

class Payments(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    service_id = models.ForeignKey(Services, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateField()
    expiration_date = models.DateField()

    class Meta:
        db_table='Api-Payments'


class Payments_expired(models.Model):
    payment_id = models.ForeignKey(Payments, on_delete=models.CASCADE)
    amount_fee = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table='Api-Payments_expired'