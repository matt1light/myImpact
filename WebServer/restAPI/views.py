from .models import Service, Device, RawData, Rate, GoalRate
from .serializer import DeviceSerializer, ServiceSerializer, RawDataSerializer, RateSerializer, GoalRateSerializer
from rest_framework import viewsets, generics
from django_filters import rest_framework as filters

class RateFilter(filters.FilterSet):
    class Meta:
        model = Rate
        fields = {
            'name': ['exact', 'in', 'startswith'],
            'time': ['gte', 'lte'],
            'device': ['exact'],
        }

class RawDataFilter(filters.FilterSet):
    class Meta:
        model = RawData
        fields = {
            'dateTime': ['gte', 'lte'],
        }

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
    filterset_class = RawDataFilter

    # def perform_create(self, serializer):
    #     pdb.set_trace()
    #     device = Device.objects.filter(board_id=self.request.boardId)
    #     if(not device):
    #         service = Service.objects.filter(name=self.request.deviceType)
    #         if(not service):
    #             # create a service, but don't add an analyzer
    #             service = Service.create(name=self.request.deviceType)
    #         device = Device.objects.create(service=service, boardId=self.request.boardId)
    #     serializer.save(device=device,
    #                     dateTime=self.request.dateTime,
    #                     deviceType=self.request.deviceType,
    #                     data=self.request.data)



class RateViewSet(viewsets.ModelViewSet):
    queryset = Rate.objects.all()
    serializer_class = RateSerializer
    filterset_class = RateFilter

class GoalRateViewSet(viewsets.ModelViewSet):
    queryset = GoalRate.objects.all()
    serializer_class = GoalRateSerializer