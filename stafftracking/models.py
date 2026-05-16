from django.db import models
from django.contrib.auth.models import User


class StaffLocation(models.Model):
    staff = models.OneToOneField(User, on_delete=models.CASCADE, related_name="location")
    latitude = models.FloatField()
    longitude = models.FloatField()
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.staff.username