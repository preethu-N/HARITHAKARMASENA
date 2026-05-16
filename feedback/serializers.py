from rest_framework import serializers
from .models import UserFeedback


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserFeedback
        fields = "__all__"
        extra_kwargs = {
            "user": {"required": False}
        }