from django.db import models
from myapp.models import Register

# Create your models here.



class WasteRequest(models.Model):
    STATUS_CHOICES = (
        ("PENDING", "PENDING"),
        ("COMPLETED", "COMPLETED"),
    )

    user = models.ForeignKey(Register, on_delete=models.CASCADE)
    waste_type = models.CharField(max_length=100)
    date = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="PENDING")

    def __str__(self):
        return self.waste_type


class Payment(models.Model):
    STATUS_CHOICES = (
        ("PAID", "PAID"),
        ("PENDING", "PENDING"),
    )

    user = models.ForeignKey(Register, on_delete=models.CASCADE)
    amount = models.IntegerField()
    invoice = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)

    def __str__(self):
        return self.invoice


class Feedback(models.Model):
    user = models.ForeignKey(Register, on_delete=models.CASCADE)
    message = models.TextField()

    def __str__(self):
        return self.user.name
