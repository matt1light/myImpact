"""

Analyzer interface

"""

import abc
import json
from .models import RawData
from .models import Rate
import sys
import datetime
import pdb

class Analyzer(abc.ABC):
#Abstract class in which services extend
    @abc.abstractmethod
    def analyze(self, dataArray):
        pass

class Trash(Analyzer):
    def analyze(self, dataArray):
        rate_object=Rate()
        data_list1=dataArray[0].data.split(" ")
        data_list2=dataArray[-1].data.split(" ")
        # finding units from arbitrary data point
        rate_object.units=data_list1[len(data_list1)-1]
        #finding rate of change
        value1 = float(data_list1[-2])
        value2 = float(data_list2[-2])
        rise = value2 - value1
        time1 = dataArray[0].dateTime
        time2 = dataArray[-1].dateTime
        deltarun = (time2-time1).days
        pdb.set_trace()
        rate_object.value=rise/deltarun
        return rate_object

class Water(Analyzer):
    def analyze(self):
        return

class Heat(Analyzer):
    def analyze(self):
        return

class Energy(Analyzer):
    def analyze(self):
        return
