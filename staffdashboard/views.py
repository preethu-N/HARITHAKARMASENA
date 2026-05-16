from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import viewsets
from .models import StaffTask
from .serializers import StaffTaskSerializer


# TASK VIEWSET
class StaffTaskViewSet(viewsets.ModelViewSet):
    queryset = StaffTask.objects.all()
    serializer_class = StaffTaskSerializer


# NOTIFICATION API (IMPORTANT FIX)
@api_view(["GET"])
def notifications_view(request):
    data = [
        {
            "id": 1,
            "title": "New Task Assigned",
            "text": "You have a new waste collection task"
        },
        {
            "id": 2,
            "title": "Reminder",
            "text": "Complete pending tasks today"
        }
    ]
    return Response(data)