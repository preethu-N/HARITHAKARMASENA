from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.exceptions import AuthenticationFailed
from myapp.models import Register


class CustomJWTAuthentication(JWTAuthentication):

    def authenticate(self, request):

        header = self.get_header(request)

        print("HEADER =", header)

        if header is None:
            return None

        raw_token = self.get_raw_token(header)

        print("RAW TOKEN =", raw_token)

        if raw_token is None:
            return None

        validated_token = self.get_validated_token(
            raw_token
        )

        print("VALIDATED TOKEN =", validated_token)

        user_id = validated_token.get(
            "user_id"
        )

        print("USER ID =", user_id)

        try:

            user = Register.objects.get(
                id=int(user_id)
            )

            print("USER =", user)

            return (user, validated_token)

        except Exception as e:

            print("AUTH ERROR =", e)

            raise AuthenticationFailed(
                "User not found"
            )