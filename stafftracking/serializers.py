from rest_framework import serializers
from .models import StaffLocation


class StaffLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = StaffLocation
        fields = "__all__"
        read_only_fields = ["staff", "updated_at"]