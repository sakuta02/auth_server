from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from authentication.models import Device, Status
from datetime import datetime
from authentication.serializers import DeviceSerializer, HandleDeviceSerializer
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import decorators, status


class DeviceAuthView(ModelViewSet):
    serializer_class = DeviceSerializer
    queryset = Device.objects

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.last_login = datetime.now()
        instance.save()
        return super().retrieve(request, *args, **kwargs)


class HandleAuthView(GenericViewSet, ListModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = HandleDeviceSerializer
    queryset = Device.objects.all()

    @decorators.action(methods=['delete'], detail=False)
    def clear(self, request):
        devices = list(Device.objects.filter(status__in=(Status.NOT_VIEWED.value, Status.DENIED.value)))
        count_devices = len(devices)
        for device in devices:
            device.delete()
        return Response(data={'count_devices': count_devices}, status=status.HTTP_204_NO_CONTENT)
