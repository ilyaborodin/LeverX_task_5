from django.urls import path, include
from .views import Test

urlpatterns = [
    path("", Test.as_view()),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
]
