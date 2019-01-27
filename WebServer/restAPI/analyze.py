"""

Analyzer interface

"""

import abc
import json
from .models import RawData
from .models import Rate
import sys
from datetime import datetime
import pdb


class Analyzer(abc.ABC):
    # Abstract class in which services extend
    @abc.abstractmethod
    def analyze(self, dataArray):
        pass


class Trash(Analyzer):
    def analyze(self, dataArray):
        rate_object = Rate()
        data_list1 = dataArray[0].data.split(" ")
        data_list2 = dataArray[-1].data.split(" ")
        # finding units from arbitrary data point
        rate_object.units = data_list1[len(data_list1) - 1] + "/day"
        # finding device ID from arbitary point
        rate_object.device = dataArray[0].device
        # time instance variable instantiation
        time = dataArray[0].dateTime.strftime("%Y-%m-%d")
        rate_object.time = datetime.strptime(time, "%Y-%m-%d")
        # finding rate of change
        value1 = float(data_list1[-2])
        value2 = float(data_list2[-2])
        rise = value2 - value1
        time1 = dataArray[0].dateTime
        time2 = dataArray[-1].dateTime
        deltarun = (time2 - time1).days
        rate_object.value = rise / deltarun
        return rate_object


class Water(Analyzer):
    def analyze(self, dataArray):
        rate_object = Rate()
        data_list1 = dataArray[0].data.split(" ")
        # finding units from arbitrary data point
        rate_object.units = data_list1[-1]
        # finding device ID from arbitary point
        rate_object.device = dataArray[0].device
        # time instance variable instantiation
        time = dataArray[0].dateTime.strftime("%Y-%m-%d")
        rate_object.time = datetime.strptime(time, "%Y-%m-%d")
        # finding L of water per day
        rate_object.value = 0.0
        for i in range(len(dataArray)):
            iterated_list = dataArray[i].data.split(" ")
            rate_object.value += float(iterated_list[-2])
        return rate_object


class Gas(Analyzer):
    def analyze(self, dataArray):
        rate_object = Rate()
        # finding device ID from arbitary point
        rate_object.device = dataArray[0].device
        # time instance variable instantiation
        time = dataArray[0].dateTime.strftime("%Y-%m-%d")
        rate_object.time = datetime.strptime(time, "%Y-%m-%d")
        # finding MJ of Gas per day
        rate_object.value = 0.0
        for i in range(len(dataArray)):
            data = json.loads(dataArray[i].data)
            rate_object.value += float(data["value"])
            if i == 0:
                rate_object.units = data["unit"]
        return rate_object


class Electricity(Analyzer):
    def analyze(self, dataArray):
        rate_object = Rate()
        pdb.set_trace()
        # finding device ID from arbitary point
        rate_object.device = dataArray[0].device
        # time instance variable instantiation
        time=dataArray[0].dateTime.strftime("%Y-%m-%d")
        rate_object.time=datetime.strptime(time, "%Y-%m-%d")
        print(rate_ob)
        # finding kWh of Electricity per day
        rate_object.value = 0.0
        for i in range(len(dataArray)):
            data = json.loads(dataArray[i].data)
            rate_object.value += float(data["value"])
            if i == 0:
                rate_object.units = data["unit"]
        return rate_object
