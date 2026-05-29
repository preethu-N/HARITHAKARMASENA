from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse, HttpResponse
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from dasboard.views import dashboard_summary


urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/', include('myapp.urls')),
    path('api/login/', include('logins.urls')),
    path('api/dashboard/', include('dasboard.urls')),
    path('api/dasboardwaste/', dashboard_summary, name='dashboard_summary'),
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

    path('', lambda request: HttpResponse("""
    

    <h3>Available Routes:</h3>

    <ul>
        <li>/admin/</li>
        <li>/api/</li>
        <li>/api/login/</li>
        <li>/api/dashboard/</li>
        <li>/api/dasboardwaste/</li>
        <li>/api/payment/</li>
        <li>/api/complaint/</li>
        <li>/api/feedback/</li>
        <li>/api/staff/</li>
        <li>/api/adminpanel/</li>
        <li>/api/booking/</li>
        <li>/api/request/</li>
        <li>/api/history/</li>
        <li>/api/tracking/</li>
        <li>/api/home/</li>
        <li>/api/token/</li>
        <li>/api/token/refresh/</li>
    </ul>
""")),
]