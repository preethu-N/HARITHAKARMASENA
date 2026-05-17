from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    NotificationViewSet,
    admin_users,
    admin_bookings,
    approve_booking,
    reject_booking,
    admin_complaints,
    resolve_complaint,
    delete_complaint
)

router = DefaultRouter()

router.register("notifications", NotificationViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("users/", admin_users),
    path("bookings/", admin_bookings),
    path("bookings/<int:pk>/approve/", approve_booking),
    path("bookings/<int:pk>/reject/", reject_booking),
    path("complaints/", admin_complaints),
    path("complaints/<int:pk>/resolve/", resolve_complaint),
    path("complaints/<int:pk>/", delete_complaint),
]