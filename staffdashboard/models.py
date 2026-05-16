from django.db import models


class StaffTask(models.Model):

    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("in-progress", "In Progress"),
        ("completed", "Completed"),
    ]

    type = models.CharField(max_length=100)

    customer = models.CharField(max_length=100)

    address = models.TextField()

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="pending"
    )

    def __str__(self):

        return self.type