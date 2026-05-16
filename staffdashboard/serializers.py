from rest_framework import serializers
from .models import StaffTask


class StaffTaskSerializer(serializers.ModelSerializer):

    class Meta:

        model = StaffTask

        fields = "__all__"