from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StaffTaskViewSet, notifications_view

router = DefaultRouter()
router.register("stafftasks", StaffTaskViewSet, basename="stafftasks")

urlpatterns = [
    path("", include(router.urls)),
    path("notifications/", notifications_view),
]