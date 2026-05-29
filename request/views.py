from rest_framework import viewsets

from .models import UserRequest
from .serializers import UserRequestSerializer


class UserRequestViewSet(
    viewsets.ModelViewSet
):

    queryset = UserRequest.objects.all()

    serializer_class = UserRequestSerializer

    def perform_create(self, serializer):
        user_request = serializer.save()
        from booking.models import Booking
        Booking.objects.create(
            user=user_request.user,
            waste_type=user_request.waste_type,
            address=user_request.address,
            status="pending"
        )