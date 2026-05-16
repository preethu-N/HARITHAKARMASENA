from rest_framework.views import APIView
from rest_framework.response import Response

class HomeView(APIView):

    def get(self, request):

        data = {
            "message": "Home API Working"
        }

        return Response(data)