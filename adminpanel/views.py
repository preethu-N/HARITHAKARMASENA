from rest_framework import viewsets

from .models import AdminNotification
from .serializers import NotificationSerializer


class NotificationViewSet(viewsets.ModelViewSet):

    queryset = AdminNotification.objects.all()

    serializer_class = NotificationSerializer

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from myapp.models import Register
from request.models import UserRequest
from complaint.models import UserComplaint
from staffdashboard.models import StaffTask

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def admin_users(request):
    users = Register.objects.all()
    data = [{"id": u.id, "name": u.name, "email": u.email, "role": u.role} for u in users]
    return Response(data)

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def admin_bookings(request):
    bookings = UserRequest.objects.all()
    data = []
    for b in bookings:
        data.append({
            "id": b.id,
            "user": b.user.name if b.user else "Unknown",
            "type": b.waste_type,
            "address": b.address,
            "status": b.status
        })
    return Response(data)

@api_view(["PATCH"])
@permission_classes([IsAuthenticated])
def approve_booking(request, pk):
    try:
        booking = UserRequest.objects.get(id=pk)
        booking.status = "APPROVED"
        booking.save()
        
        # Create staff task
        StaffTask.objects.create(
            type=booking.waste_type,
            customer=booking.user.name if booking.user else "Unknown",
            address=booking.address,
            status="pending",
            request_id=booking.id
        )
        
        # Create admin notification
        AdminNotification.objects.create(
            title="Booking Approved",
            message=f"Booking #{booking.id} assigned to staff."
        )
        
        return Response({
            "id": booking.id,
            "user": booking.user.name if booking.user else "Unknown",
            "type": booking.waste_type,
            "address": booking.address,
            "status": booking.status
        })
    except Exception as e:
        return Response({"error": str(e)}, status=400)

@api_view(["PATCH"])
@permission_classes([IsAuthenticated])
def reject_booking(request, pk):
    try:
        booking = UserRequest.objects.get(id=pk)
        booking.status = "REJECTED"
        booking.save()
        return Response({
            "id": booking.id,
            "user": booking.user.name if booking.user else "Unknown",
            "type": booking.waste_type,
            "address": booking.address,
            "status": booking.status
        })
    except Exception as e:
        return Response({"error": str(e)}, status=400)

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def admin_complaints(request):
    complaints = UserComplaint.objects.all()
    data = []
    for c in complaints:
        data.append({
            "id": c.id,
            "user": c.user.name if c.user else "Unknown",
            "subject": c.subject,
            "message": c.message,
            "status": c.status
        })
    return Response(data)

@api_view(["PATCH"])
@permission_classes([IsAuthenticated])
def resolve_complaint(request, pk):
    try:
        complaint = UserComplaint.objects.get(id=pk)
        complaint.status = "resolved"
        complaint.save()
        return Response({
            "id": complaint.id,
            "user": complaint.user.name if complaint.user else "Unknown",
            "subject": complaint.subject,
            "message": complaint.message,
            "status": complaint.status
        })
    except Exception as e:
        return Response({"error": str(e)}, status=400)

@api_view(["DELETE"])
@permission_classes([IsAuthenticated])
def delete_complaint(request, pk):
    try:
        complaint = UserComplaint.objects.get(id=pk)
        complaint.delete()
        return Response({"message": "Deleted"})
    except Exception as e:
        return Response({"error": str(e)}, status=400)