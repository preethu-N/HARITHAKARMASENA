from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StaffLocationViewSet

router = DefaultRouter()
router.register("tracking", StaffLocationViewSet, basename="tracking")

urlpatterns = [
    path("", include(router.urls)),
]