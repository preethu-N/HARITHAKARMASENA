from django.db import models
from django.contrib.auth.models import User


class UserComplaint(models.Model):

    STATUS_CHOICES = (
        ("pending", "pending"),
        ("resolved", "resolved"),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    subject = models.CharField(max_length=200)

    message = models.TextField()

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="pending"
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject
