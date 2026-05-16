from rest_framework import serializers
from .models import UserComplaint


class ComplaintSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserComplaint
        fields = "__all__"