from rest_framework.response import Response
from rest_framework.decorators import api_view, action
from rest_framework import viewsets
from rest_framework import status
from .models import StaffTask
from .serializers import StaffTaskSerializer


# TASK VIEWSET
class StaffTaskViewSet(viewsets.ModelViewSet):
    queryset = StaffTask.objects.all()
    serializer_class = StaffTaskSerializer

    @action(detail=True, methods=['put'], url_path='start')
    def start(self, request, pk=None):
        """Start a task (change status to in-progress)"""
        task = self.get_object()
        task.status = "in-progress"
        task.save()

        # Update corresponding Booking and UserRequest
        if task.request_id:
            from booking.models import Booking
            from request.models import UserRequest

            Booking.objects.filter(pk=task.request_id).update(status="scheduled")
            booking = Booking.objects.filter(pk=task.request_id).first()
            if booking:
                UserRequest.objects.filter(
                    user=booking.user,
                    waste_type=booking.waste_type,
                    address=booking.address
                ).update(status="in-progress")

        serializer = self.get_serializer(task)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=True, methods=['put'], url_path='complete')
    def complete(self, request, pk=None):
        """Complete a task (change status to completed)"""
        task = self.get_object()
        task.status = "completed"
        task.save()

        # Update corresponding Booking and UserRequest
        if task.request_id:
            from booking.models import Booking
            from request.models import UserRequest

            booking = Booking.objects.filter(pk=task.request_id).first()
            if booking:
                UserRequest.objects.filter(
                    user=booking.user,
                    waste_type=booking.waste_type,
                    address=booking.address
                ).update(status="completed")

        serializer = self.get_serializer(task)
        return Response(serializer.data, status=status.HTTP_200_OK)


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