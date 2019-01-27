"""

Analyzer interface

"""

import abc
import json
from models import RawData
from models import Rate


class Analyzer(abc.ABC):
#Abstract class in which services extend
    @abc.abstractmethod
    def analyze(self):
        pass

class Trash(analyzer):
    @staticmethod
    def analyze(self, dataArray):
        rate_object=Rate()
        data_list1=dataArray[0].data.split(" ")
        data_list2=dataArray[len(dataArray)-1].data.split(" ")
        # finding units from arbitrary data point
        rate_object.units=word_list[len(word_list)-1]
        #finding rate of change
        rate_object.value=(float(data_list1[len(data_list1)-2])-float(data_list2[len(data_list2)-2]))/abs(dataArray[len(dataArray-1)].time()-dataArray[0].time())
        return rate_object

class Water(analyzer):
    @staticmethod
    def analyze(self):

class Heat(analyzer):
    @staticmethod
    def analyze(self):

class Energy(analyzer):
    @staticmethod
    def analyze(self):

