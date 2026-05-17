from django.db import models
from myapp.models import Register


class StaffLocation(models.Model):
    staff = models.OneToOneField(Register, on_delete=models.CASCADE, related_name="location")
    latitude = models.FloatField()
    longitude = models.FloatField()
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.staff.name