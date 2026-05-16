from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import WasteRequestViewSet, PaymentViewSet, FeedbackViewSet

router = DefaultRouter()
router.register(r'waste', WasteRequestViewSet)
router.register(r'payment', PaymentViewSet)
router.register(r'feedback', FeedbackViewSet)

urlpatterns = [
    path('', include(router.urls)),
]