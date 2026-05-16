from rest_framework import serializers
from .models import AdminNotification


class NotificationSerializer(serializers.ModelSerializer):

    class Meta:
        model = AdminNotification
        fields = "__all__"