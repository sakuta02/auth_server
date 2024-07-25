from rest_framework.viewsets import ModelViewSet, GenericViewSet
from authentication.models import Device
from datetime import datetime
from authentication.serializers import DeviceSerializer, HandleDeviceSerializer
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


class DeviceAuthView(ModelViewSet):
    serializer_class = DeviceSerializer
    queryset = Device.objects

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.last_login = datetime.now()
        instance.save()
        return super().retrieve(request, *args, **kwargs)


class HandleAuthView(GenericViewSet, ListModelMixin, RetrieveModelMixin, UpdateModelMixin):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = HandleDeviceSerializer
    queryset = Device.objects.all()
