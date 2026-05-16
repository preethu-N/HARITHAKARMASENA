from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from myapp.models import Register
import json
import uuid

# simple fake token generator (for now)
def generate_token():
    return str(uuid.uuid4())


@csrf_exempt
def login_view(request):

    if request.method == "POST":

        data = json.loads(request.body)

        email = data.get("email")
        password = data.get("password")

        try:
            user = Register.objects.get(email=email)

            if user.password == password:

                token = generate_token()

                return JsonResponse({
                    "message": "Login Success",
                    "access": token,   # ✅ ADD THIS
                    "role": user.role,
                    "user": {
                        "id": user.id,
                        "name": user.name,
                        "email": user.email,
                        "role": user.role,
                    }
                })

            else:
                return JsonResponse({
                    "error": "Invalid password"
                }, status=401)

        except Register.DoesNotExist:
            return JsonResponse({
                "error": "User not found"
            }, status=404)