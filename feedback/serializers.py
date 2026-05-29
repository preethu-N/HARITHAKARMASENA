from rest_framework import serializers
from .models import UserFeedback


class FeedbackSerializer(serializers.ModelSerializer):

    class Meta:

        model = UserFeedback

        fields = [
            "id",
            "subject",
            "message",
            "created_at",
        ]