from .models import Service, Device, RawData, Rate
from .serializer import DeviceSerializer, ServiceSerializer, RawDataSerializer, RateSerializer

# Create your views here.

class DeviceViewSet():
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer

class ServiceViewSet():
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

class RawDataViewSet():
    queryset = RawData.objects.all()
    serializer_class = RawDataSerializer

class RateViewSet():
    queryset = Rate.objects.all()
    serializer_class = RateSerializer
