from django.db import models


class Register(models.Model):

    ROLE_CHOICES = (
        ('USER', 'USER'),
        ('STAFF', 'STAFF'),
        ('ADMIN', 'ADMIN'),
    )

    name = models.CharField(max_length=100)

    email = models.EmailField(unique=True)

    password = models.CharField(max_length=100)

    phone = models.CharField(max_length=15)

    address = models.TextField()

    role = models.CharField(
        max_length=10,
        choices=ROLE_CHOICES,
        default='USER'
    )

    def __str__(self):
        return self.name