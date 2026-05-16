from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import UserRequestViewSet

router = DefaultRouter()

router.register(
    "requests",
    UserRequestViewSet,
    basename="requests"
)

urlpatterns = [
    path("", include(router.urls)),
]