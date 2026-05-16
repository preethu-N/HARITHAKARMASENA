from rest_framework.views import APIView
from rest_framework.response import Response

from request.models import UserRequest
from payment.models import UserPayment


class HistoryView(APIView):

    def get(self, request):

        user = request.user

        requests = UserRequest.objects.filter(user=user)
        payments = UserPayment.objects.filter(user=user)

        data = []

        for r in requests:

            paid = payments.filter(
                payment_type=r.waste_type,
                status="PAID"
            ).exists()

            data.append({
                "id": r.id,
                "type": r.waste_type,
                "date": r.date,
                "status": r.status,
                "payment": "PAID" if paid else "PENDING"
            })

        return Response(data)