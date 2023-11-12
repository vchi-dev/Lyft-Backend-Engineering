import unittest
from datetime import datetime

from battery.nubbin_battery import NubbinBattery


class TestBattery(unittest.TestCase):

    # Digital Ocean Guide to Date
    # from datetime import datetime

    # date_str = '09-19-2022'

    # date_object = datetime.strptime(date_str, '%m-%d-%Y').date()
    # print(type(date_object))
    # print(date_object)  # printed in default format


    def nubbin_not_need_1(self):
        current, last = '09-19-2022', '10-10-2020'
        date_current = datetime.strptime(current, '%m-%d-%Y').date()
        date_last = datetime.strptime(last, '%m-%d-%Y').date()
        car = NubbinBattery(date_last, date_current)
        self.assertFalse(car.needs_service())

    def nubbin_need_1(self):
        current, last = '09-19-2025', '10-10-2020'
        date_current = datetime.strptime(current, '%m-%d-%Y').date()
        date_last = datetime.strptime(last, '%m-%d-%Y').date()
        car = NubbinBattery(date_last, date_current)
        self.assertTrue(car.needs_service())

    def spindler_not_need_1(self):
        current, last = '09-19-2023', '10-10-2020'
        date_current = datetime.strptime(current, '%m-%d-%Y').date()
        date_last = datetime.strptime(last, '%m-%d-%Y').date()
        car = NubbinBattery(date_last, date_current)
        self.assertFalse(car.needs_service())

    def spindler_need_1(self):
        current, last = '09-19-2024', '10-10-2020'
        date_current = datetime.strptime(current, '%m-%d-%Y').date()
        date_last = datetime.strptime(last, '%m-%d-%Y').date()
        car = NubbinBattery(date_last, date_current)
        self.assertTrue(car.needs_service())