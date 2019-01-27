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

class RawDataSerializer(serializers.Serializer):
    deviceType = serializers.CharField()
    boardId = serializers.CharField()
    dateTime = serializers.DateTimeField()
    data = serializers.CharField()

    def create(self, validated_data):
        device = Device.objects.filter(boardId=validated_data['boardId'])
        if(not device):
            service = Service.objects.filter(name=validated_data['deviceType'])
            if(not service):
                # create a service, but don't add an analyzer
                service = Service.objects.create(name=validated_data['deviceType'])
            else:
                service = service[0]
            device = Device.objects.create(service=service, boardId=validated_data['boardId'])
        else:
            device = device[0]
        raw_data = RawData.objects.create(device=device,
                        dateTime=validated_data['dateTime'],
                        deviceType=validated_data['deviceType'],
                        data=validated_data['data'],
                        boardId=validated_data['boardId'])
        return raw_data



class RateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Rate
        fields = ('name', 'units', 'time', 'value')

class GoalRateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = GoalRate
        fields = ('level', 'value', 'service')