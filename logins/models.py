from django.db import models


class User(models.Model):

    ROLE_CHOICES = (
        ('USER', 'USER'),
        ('STAFF', 'STAFF'),
        ('ADMIN', 'ADMIN'),
    )

    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    def __str__(self):
        return self.email