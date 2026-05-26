from django.urls import path
from .views import login_view
from rest_framework_simplejwt.views import TokenObtainPairView


urlpatterns = [
    path('', login_view),
]