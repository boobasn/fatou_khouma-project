from rest_framework import serializers
from .models import Device
from .models import SensorReading
class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = '__all__'