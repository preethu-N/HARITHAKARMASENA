from rest_framework import serializers
from .models import WasteRequest, Payment, Feedback


class WasteRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = WasteRequest
        fields = "__all__"


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = "__all__"


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = "__all__"