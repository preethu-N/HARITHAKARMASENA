from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.tokens import AccessToken
from myapp.models import Register

class CustomJWTAuthentication(BaseAuthentication):
    def authenticate(self, request):
        auth_header = request.headers.get('Authorization')
        
        if not auth_header or not auth_header.startswith('Bearer '):
            return None
            
        token = auth_header.split(' ')[1]
        
        try:
            validated_token = AccessToken(token)
            user_id = validated_token['user_id']
            user = Register.objects.get(id=user_id)
            # DRF needs is_authenticated to pass the permission check
            user.is_authenticated = True
            return (user, validated_token)
            
        except Register.DoesNotExist:
            raise AuthenticationFailed('User not found')
        except Exception as e:
            raise AuthenticationFailed('Invalid or expired token')
