from rest_framework.viewsets import ModelViewSet
from authentication.models import Device
from authentication.serializers import DeviceSerializer


class DeviceAuthView(ModelViewSet):
    serializer_class = DeviceSerializer
    queryset = Device.objects.all()
