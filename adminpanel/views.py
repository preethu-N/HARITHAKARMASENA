from rest_framework import viewsets

from .models import AdminNotification
from .serializers import NotificationSerializer


class NotificationViewSet(viewsets.ModelViewSet):

    queryset = AdminNotification.objects.all()

    serializer_class = NotificationSerializer