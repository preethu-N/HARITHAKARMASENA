from django.shortcuts import render
from rest_framework import viewsets

from .models import UserPayment
from .serializers import PaymentSerializer


class PaymentViewSet(viewsets.ModelViewSet):

    queryset = UserPayment.objects.all()
    serializer_class = PaymentSerializer