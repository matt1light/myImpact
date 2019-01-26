from django.db import models



#your models here.

class Service(models.Model):
    name = models.TextField()
    analyzer = models.TextField()
    description = models.TextField()

class Device(models.Model):
    name = models.TextField()
    id = models.IntegerField()
    service = models.ForeignKey(Service, related_name = 'devices', on_delete=models.SET_NULL, null=True)

class RawData(models.Model):
    device = models.ForeignKey(Service, related_name = 'raw_datas', on_delete = models.CASCADE)
    time = models.DateTimeField()
    data = models.TextField()

class Rate(models.Model):
    name = models.CharField(max_length=50)
    units = models.CharField(max_length=20)
    time = models.DateTimeField()
    value = models.FloatField()
