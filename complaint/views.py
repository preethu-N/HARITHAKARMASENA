from rest_framework import viewsets

from .models import UserComplaint
from .serializers import ComplaintSerializer


class ComplaintViewSet(viewsets.ModelViewSet):

    queryset = UserComplaint.objects.all()

    serializer_class = ComplaintSerializer
