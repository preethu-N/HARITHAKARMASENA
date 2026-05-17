from django.db import models
from myapp.models import Register


class UserRequest(models.Model):

    STATUS_CHOICES = (
        ("PENDING", "PENDING"),
        ("APPROVED", "APPROVED"),
        ("REJECTED", "REJECTED"),
        ("in-progress", "in-progress"),
        ("completed", "completed"),
    )

    user = models.ForeignKey(
        Register,
        on_delete=models.CASCADE,
        related_name="userrequests"
    )

    waste_type = models.CharField(max_length=50)

    date = models.DateField()

    address = models.TextField()

    fee = models.IntegerField(default=0)

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="PENDING"
    )

    def __str__(self):
        return self.waste_type