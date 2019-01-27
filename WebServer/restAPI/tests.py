from django.test import TestCase
from .models import RawData, Rate
from analyzer import trash
import datetime

# Create your tests here.

class AnalyzerTests(TestCase):
    def setUp(self):
        today=datetime.datetime.now()
        self.raw_data_array = []
        for x in range(0, 10):
            data = "{\d\d " + str(x) +"kg }"
            self.raw_data_array.append(
                RawData(
                    dateTime= today.replace(day=today.day+x),
                    deviceType= "trash",
                    data = data,
                    boardId= "X1D54"))

    def testZeroToTen(self):
         trash_analyzer = Trash()
         rate = trash_analyzer.analyze(self.raw_data_array)
         print(rate.time)
         print(rate.units)
         print(rate.device)
         print(rate.name)
         print(rate.value)
