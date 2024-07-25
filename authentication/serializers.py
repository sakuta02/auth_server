from rest_framework.serializers import ModelSerializer
from authentication.models import Device


class DeviceSerializer(ModelSerializer):

    class Meta:
        model = Device
        fields = ("device_id", "status")
        read_only_fields = ("status", )
