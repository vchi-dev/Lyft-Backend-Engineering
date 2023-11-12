import unittest
# from datetime import datetime

from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine

class TestEngine(unittest.TestCase):

    # An easy case
    def capulet_not_need_1(self):
        current_mileage, last_service_mileage = 100, 100
        car = CapuletEngine(current_mileage, last_service_mileage)
        self.assertFalse(car.needs_service())

    # Edge case for not needed
    def capulet_not_need_2(self):
        current_mileage, last_service_mileage = 31000, 1000
        car = CapuletEngine(current_mileage, last_service_mileage)
        self.assertFalse(car.needs_service())

    # Edge case for needed
    def capulet_need_1(self):
        current_mileage, last_service_mileage = 31000, 999
        car = CapuletEngine(current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service())

    # An easy case
    def capulet_need_2(self):
        current_mileage, last_service_mileage = 31000, 100
        car = CapuletEngine(current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service())

    def sternman_need_1(self):
        car = SternmanEngine(True)
        self.assertTrue(car.needs_service())

    def sternman_not_need_1(self):
        car = SternmanEngine(False)
        self.assertFalse(car.needs_service())

    # An easy case
    def willoughby_not_need_1(self):
        current_mileage, last_service_mileage = 100, 100
        car = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertFalse(car.needs_service())

    # Edge case for not needed
    def willoughby_not_need_2(self):
        current_mileage, last_service_mileage = 61000, 1000
        car = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertFalse(car.needs_service())

    # Edge case for needed
    def willoughby_need_1(self):
        current_mileage, last_service_mileage = 61000, 999
        car = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service())

    # An easy case
    def willoughby_need_2(self):
        current_mileage, last_service_mileage = 61000, 100
        car = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service())