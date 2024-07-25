from django.urls import path, include
from rest_framework.routers import SimpleRouter
from authentication.views import DeviceAuthView, HandleAuthView

rt = SimpleRouter()
rt.register('handle-devices', HandleAuthView, basename='handle-devices')

urlpatterns = [
    path('devices/<pk>', DeviceAuthView.as_view({'get': 'retrieve'}), name='auth'),
    path('devices/', DeviceAuthView.as_view({'post': 'create'}), name='auth'),
    path('', include(rt.urls))
]
