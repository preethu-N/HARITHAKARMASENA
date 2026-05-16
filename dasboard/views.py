from rest_framework import viewsets
from .models import WasteRequest, Payment, Feedback
from .serializers import WasteRequestSerializer, PaymentSerializer, FeedbackSerializer

class WasteRequestViewSet(viewsets.ModelViewSet):
    queryset = WasteRequest.objects.all()
    serializer_class = WasteRequestSerializer

class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

class FeedbackViewSet(viewsets.ModelViewSet):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer