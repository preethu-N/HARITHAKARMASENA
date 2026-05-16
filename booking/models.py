from django.db import models
from django.contrib.auth.models import User


class Booking(models.Model):

    STATUS_CHOICES = (
        ("pending", "pending"),
        ("approved", "approved"),
        ("rejected", "rejected"),
        ("scheduled", "scheduled"),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    waste_type = models.CharField(max_length=100)

    address = models.TextField()

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="pending"
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.waste_type