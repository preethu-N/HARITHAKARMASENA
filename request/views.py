from rest_framework import viewsets

from .models import UserRequest
from .serializers import UserRequestSerializer


class UserRequestViewSet(
    viewsets.ModelViewSet
):

    queryset = UserRequest.objects.all()

    serializer_class = UserRequestSerializer