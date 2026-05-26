from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from myapp.models import Register
import json
from rest_framework_simplejwt.tokens import RefreshToken


def generate_token(user):
    refresh = RefreshToken.for_user(user)
    return str(refresh.access_token)


@csrf_exempt
def login_view(request):

    if request.method != "POST":
        return JsonResponse({
            "error": "Method not allowed"
        }, status=405)

    try:
        data = json.loads(request.body)

        email = data.get("email")
        password = data.get("password")

        # Check standard Django User by email or username to see if they are a superuser
        from django.contrib.auth.models import User as DjangoUser
        from django.db.models import Q

        django_superuser = DjangoUser.objects.filter(is_superuser=True).filter(
            Q(email__iexact=email) | Q(username__iexact=email)
        ).first()

        if django_superuser:

            # Block the old admin accounts
            blocked_admins = ["admin@gmail.com", "achu@gmail.com"]

            if django_superuser.email in blocked_admins or django_superuser.username in blocked_admins:
                return JsonResponse({
                    "error": "This admin account is blocked. Please create a new superuser."
                }, status=403)

            if django_superuser.check_password(password):

                # Ensure Register entry exists
                user, created = Register.objects.get_or_create(
                    email=django_superuser.email or email,
                    defaults={
                        "name": django_superuser.username or "Admin",
                        "password": "",
                        "phone": "",
                        "address": "",
                        "role": "ADMIN",
                    }
                )

                role = "admin"

                token = generate_token(user)

                return JsonResponse({
                    "message": "Login Success",
                    "access": token,
                    "role": role,
                    "user": {
                        "id": user.id,
                        "name": user.name,
                        "email": user.email,
                        "role": role,
                    }
                })

            else:
                return JsonResponse({
                    "error": "Invalid password"
                }, status=401)

        # Fallback to standard Register model for USER / STAFF
        user = Register.objects.get(email=email)

        if user.password == password:

            # Block ADMIN role users from normal login
            if user.role in ["ADMIN", "admin"] or user.email in ["admin@gmail.com", "achu@gmail.com"]:
                return JsonResponse({
                    "error": "Admin login must use a new superuser account"
                }, status=403)

            role = user.role

            token = generate_token(user)

            return JsonResponse({
                "message": "Login Success",
                "access": token,
                "role": role,
                "user": {
                    "id": user.id,
                    "name": user.name,
                    "email": user.email,
                    "role": role,
                }
            })

        return JsonResponse({
            "error": "Invalid password"
        }, status=401)

    except Register.DoesNotExist:
        return JsonResponse({
            "error": "User not found"
        }, status=404)

    except Exception as e:
        return JsonResponse({
            "error": str(e)
        }, status=500)