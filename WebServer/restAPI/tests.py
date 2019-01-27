from django.test import TestCase
from .models import RawData, Rate
from .analyze import Gas
import datetime

# Create your tests here.

class AnalyzerTests(TestCase):
    def setUp(self):
        today=datetime.datetime.now()
        self.raw_data_array = []
        for x in range(0, 23):
            data ='{"value":' + str(x*10) + ', "unit": "MJ"}'

            self.raw_data_array.append(
                RawData(
                    dateTime= today.replace(hour=0 + x),
                    deviceType= "gas",
                    data = data,
                    boardId= "X1D54"))

    def testZeroToTen(self):
         gas_analyzer = Gas()
         rate = gas_analyzer.analyze(self.raw_data_array)
         print(rate.time)
         print(rate.units)
         print(rate.device)
         print(rate.name)
         print(rate.value)