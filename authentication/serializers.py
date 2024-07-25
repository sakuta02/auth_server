from rest_framework.serializers import ModelSerializer

from authentication.models import Device, Status


class DeviceSerializer(ModelSerializer):
    class Meta:
        model = Device
        fields = ("device_id", "status", "subscription_expires_date")
        read_only_fields = ("status", "subscription_expires_date")

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if not representation.get('subscription_expires_date'):
            representation.pop('subscription_expires_date')
        representation['status'] = Status[instance.status].value
        return representation


class HandleDeviceSerializer(ModelSerializer):
    class Meta:
        model = Device
        fields = ("device_id", "status", "subscription_expires_date", "registration_date", "last_login_date")
        read_only_fields = ("registration_date", "last_login_date")
