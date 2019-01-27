from rest_framwork import viewsets
from rest_framework_filters as filters

class DeviceFilters(filters.FilterSet):

    class Meta:
        model = Device
        fields = {
            'name'
        }

class RateFilter(filters.FilterSet):
    device filters.RelatedFilter(DeviceFilter, field_name='device', queryset=Device.objects.all())

    class Meta:
        model = Rate
        fields = {
            'name': ['exact', 'in', 'startswith'],
            'time': ['lte', 'gte']
        }

class RawDataFilter(filters.FilterSet):
    class Meta:
        model = RawData
        fields = {
            'datTime': ['lte', 'gte']
        }
