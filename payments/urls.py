from django.urls import path
from .views import PaymentList, PaymentDetailView
from .views import MyTokenObtainPairView




from rest_framework_simplejwt.views import (
    TokenRefreshView,
)


urlpatterns = [
    path('', PaymentList.as_view()),
    path('<int:id>', PaymentDetailView.as_view()),
]