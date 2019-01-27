from .models import Rate, RawData, GoalRate, Device, Service
from rest_framework import serializers


class ServiceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Service
        fields = ('name', 'analyzer', 'description')

class DeviceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Device
        fields = ('name', 'deviceId', 'service')

class RawDataSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RawData
        fields = ('device', 'time', 'data', 'date')

class RateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Rate
        fields = ('name', 'units', 'time', 'value')

class GoalRateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = GoalRate
        fields = ('level', 'value', 'service')