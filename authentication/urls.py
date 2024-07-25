from django.urls import path, include
from rest_framework.routers import DefaultRouter
from authentication.views import DeviceAuthView

rt = DefaultRouter()
rt.register('auth', DeviceAuthView, basename='auth')

urlpatterns = [
    path('', include(rt.urls))
]
