from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/', include('myapp.urls')),
    path('api/login/', include('logins.urls')),
    path('api/dashboard/', include('dasboard.urls')),
    path('api/payment/', include('payment.urls')),
    path('api/complaint/', include('complaint.urls')),
    path('api/feedback/', include('feedback.urls')),
    path('api/staff/', include('staffdashboard.urls')),
    path('api/adminpanel/', include('adminpanel.urls')),
    path('api/booking/', include('booking.urls')),
    path('api/request/', include('request.urls')),
    path('api/history/', include('history.urls')),
    path('api/tracking/', include('stafftracking.urls')),
    path('api/home/', include('homeapp.urls')),
    path('api/token/', TokenObtainPairView.as_view()),
    path('api/token/refresh/', TokenRefreshView.as_view()),
]