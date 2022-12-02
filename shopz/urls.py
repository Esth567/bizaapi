from django.urls import path
from .views import StoresList, StoresDetailView
from .views import MyTokenObtainPairView
from . import views




from rest_framework_simplejwt.views import (
    TokenRefreshView,
)


urlpatterns = [
    path('', StoresList.as_view()),
    path('<int:id>', StoresDetailView.as_view()),
    path('upload/', views.image_upload_view)
]