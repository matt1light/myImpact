from .models import Service, Device, RawData, Rate, GoalRate
from .serializer import DeviceSerializer, ServiceSerializer, RawDataSerializer, RateSerializer, GoalRateSerializer
from rest_framework import viewsets, generics

# Create your views here.

class DeviceViewSet(viewsets.ModelViewSet):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer

class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

class RawDataViewSet(viewsets.ModelViewSet):
    queryset = RawData.objects.all()
    serializer_class = RawDataSerializer

class RateViewSet(viewsets.ModelViewSet):
    queryset = Rate.objects.all()
    serializer_class = RateSerializer

class GoalRateViewSet(viewsets.ModelViewSet):
    queryset = GoalRate.objects.all()
    serializer_class = GoalRateSerializer