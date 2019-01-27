from django.db import models



#your models here.

class House(models.Model):
    occupants = models.IntegerField()

class Service(models.Model):
    name = models.TextField()
    analyzer = models.TextField(null=True, default=None)
    description = models.TextField(null=True, default=True)

class Device(models.Model):
    name = models.TextField()
    boardId = models.TextField()
    service = models.ForeignKey(Service, related_name='devices', on_delete=models.SET_NULL, null=True)
    house = models.ForeignKey(House, related_name='devices', on_delete=models.SET_NULL, null=True)

class RawData(models.Model):
    device = models.ForeignKey(Device, related_name='raw_datas', on_delete=models.CASCADE, null=True)
    dateTime = models.DateTimeField()
    deviceType = models.TextField()
    boardId = models.TextField(null=True)
    data = models.TextField()

class Rate(models.Model):
    name = models.CharField(max_length=50)
    units = models.CharField(max_length=20)
    time = models.DateTimeField()
    value = models.FloatField()
    device = models.ForeignKey(Device, related_name='rates', on_delete=models.CASCADE)

class GoalRate(models.Model):
    name = models.CharField(max_length=100)
    service = models.ForeignKey(Service, related_name='goal_rates', on_delete=models.CASCADE)
    level = models.CharField(max_length=20, default="average")
    value = models.FloatField()
    units = models.CharField(max_length=20)