from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny

from myapp.models import Register
from .serializers import RegisterSerializer


class RegisterView(APIView):

    permission_classes = [AllowAny]   # ✅ ADD THIS

    def post(self, request):

        print(request.data)

        serializer = RegisterSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(
                {"message": "Registration Successful"},
                status=status.HTTP_201_CREATED
            )

        print(serializer.errors)

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )