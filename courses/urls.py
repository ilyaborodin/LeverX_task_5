from django.urls import path, include
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
]
