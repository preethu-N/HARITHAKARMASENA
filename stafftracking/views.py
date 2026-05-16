from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import StaffLocation
from .serializers import StaffLocationSerializer


class StaffLocationViewSet(viewsets.ModelViewSet):
    serializer_class = StaffLocationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return StaffLocation.objects.filter(staff=self.request.user)

    def perform_create(self, serializer):
        serializer.save(staff=self.request.user)