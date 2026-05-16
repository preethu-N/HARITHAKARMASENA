from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class HistoryView(APIView):

    def get(self, request):

        data = [
            {
                "id": 1,
                "waste_type": "Plastic",
                "points": 20
            }
        ]

        return Response(data, status=status.HTTP_200_OK)