from rest_framework import status, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import AdminNotification
from .serializers import NotificationSerializer
from myapp.models import Register
from booking.models import Booking
from complaint.models import UserComplaint


class NotificationViewSet(viewsets.ModelViewSet):

    queryset = AdminNotification.objects.all()

    serializer_class = NotificationSerializer


@api_view(["GET"])
def admin_users(request):
    users = Register.objects.all().values("id", "name", "email", "role")
    return Response(list(users))


@api_view(["GET"])
def admin_bookings(request):
    bookings = Booking.objects.select_related("user").all().order_by("-created_at")
    payload = [
        {
            "id": booking.id,
            "user": booking.user.name,
            "type": booking.waste_type,
            "address": booking.address,
            "status": booking.status,
        }
        for booking in bookings
    ]
    return Response(payload)


@api_view(["PATCH"])
def approve_booking(request, pk):
    try:
        booking = Booking.objects.get(pk=pk)
    except Booking.DoesNotExist:
        return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)
    booking.status = "approved"
    booking.save()

    # Sync corresponding UserRequest
    from request.models import UserRequest
    UserRequest.objects.filter(
        user=booking.user,
        waste_type=booking.waste_type,
        address=booking.address,
        status="PENDING"
    ).update(status="APPROVED")

    # Auto-create StaffTask for this booking
    from staffdashboard.models import StaffTask
    StaffTask.objects.get_or_create(
        request_id=booking.id,
        defaults={
            "type": booking.waste_type,
            "customer": booking.user.name,
            "address": booking.address,
            "status": "pending",
        }
    )

    return Response(
        {
            "id": booking.id,
            "user": booking.user.name,
            "type": booking.waste_type,
            "address": booking.address,
            "status": booking.status,
        }
    )


@api_view(["PATCH"])
def reject_booking(request, pk):
    try:
        booking = Booking.objects.get(pk=pk)
    except Booking.DoesNotExist:
        return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)
    booking.status = "rejected"
    booking.save()

    # Sync corresponding UserRequest
    from request.models import UserRequest
    UserRequest.objects.filter(
        user=booking.user,
        waste_type=booking.waste_type,
        address=booking.address,
        status="PENDING"
    ).update(status="REJECTED")

    return Response(
        {
            "id": booking.id,
            "user": booking.user.name,
            "type": booking.waste_type,
            "address": booking.address,
            "status": booking.status,
        }
    )


@api_view(["GET"])
def admin_complaints(request):
    complaints = UserComplaint.objects.select_related("user").all().order_by("-created_at")
    payload = [
        {
            "id": complaint.id,
            "user": complaint.user.name,
            "subject": complaint.subject,
            "message": complaint.message,
            "status": complaint.status,
        }
        for complaint in complaints
    ]
    return Response(payload)


@api_view(["PATCH"])
def resolve_complaint(request, pk):
    try:
        complaint = UserComplaint.objects.get(pk=pk)
    except UserComplaint.DoesNotExist:
        return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)
    complaint.status = "resolved"
    complaint.save()
    return Response(
        {
            "id": complaint.id,
            "user": complaint.user.name,
            "subject": complaint.subject,
            "message": complaint.message,
            "status": complaint.status,
        }
    )


@api_view(["DELETE"])
def delete_complaint(request, pk):
    try:
        complaint = UserComplaint.objects.get(pk=pk)
    except UserComplaint.DoesNotExist:
        return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)
    complaint.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
