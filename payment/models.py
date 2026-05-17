from django.db import models
from myapp.models import Register


# Create your models here.



class UserPayment(models.Model):

    STATUS_CHOICES = (
        ("PAID", "PAID"),
        ("PENDING", "PENDING"),
    )

    user = models.ForeignKey(Register, on_delete=models.CASCADE)

    payment_type = models.CharField(max_length=100)

    amount = models.IntegerField()

    card_number = models.CharField(max_length=20)

    expiry = models.CharField(max_length=10)

    cvc = models.CharField(max_length=5)

    status = models.CharField(max_length=20, choices=STATUS_CHOICES)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.payment_type