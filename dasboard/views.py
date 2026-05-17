from rest_framework import viewsets
from .models import WasteRequest, Payment, Feedback
from .serializers import WasteRequestSerializer, PaymentSerializer, FeedbackSerializer

class WasteRequestViewSet(viewsets.ModelViewSet):
    queryset = WasteRequest.objects.all()
    serializer_class = WasteRequestSerializer

class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

class FeedbackViewSet(viewsets.ModelViewSet):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def dashboard_summary(request):
    try:
        # Avoid 500 error if models still point to User instead of Register
        requests = WasteRequest.objects.all() # Just return all for now to avoid breaking
        
        total = requests.count()
        pending = requests.filter(status="PENDING").count()
        completed = requests.filter(status="COMPLETED").count()
        points = completed * 10
        
        activities = []
        for req in requests[:5]:
            activities.append({
                "type": req.waste_type,
                "date": str(req.date),
                "status": req.status
            })
            
        return Response({
            "total": total,
            "pending": pending,
            "completed": completed,
            "points": points,
            "activities": activities
        })
    except Exception as e:
        return Response({"error": str(e)}, status=500)