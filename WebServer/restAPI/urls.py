# define our URLs here

from django.conf.urls import url, include
from rest_framework import routers
from .views import DeviceViewSet, RateViewSet, RawDataViewSet, ServiceViewSet


urlpatterns = [
    url(r'^devices/', DeviceViewSet),
    url(r'^services/', ServiceViewSet),
    url(r'^rates/', RateViewSet),
    url(r'^raw_datas/', RawDataViewSet),
]