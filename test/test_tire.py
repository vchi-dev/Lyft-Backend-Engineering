import unittest
# from datetime import datetime

from tire.carrigan import Carrigan
from tire.octoprime import Octoprime

class TestEngine(unittest.TestCase):

    def carrigan_not_need(self):
        tires = [0.4, 0.2, 0, 0]
        car = Carrigan(tires)
        self.assertFalse(car.needs_service())

    def carrigan_need(self):
        tires = [0.4, 1, 0, 0]
        car = Carrigan(tires)
        self.assertTrue(car.needs_service())

    def octoprime_not_need(self):
        tires = [0.4, 0.2, 0, 0.9]
        car = Octoprime(tires)
        self.assertFalse(car.needs_service())

    def octoprime_need(self):
        tires = [0.4, 1, 0.9, 0.9]
        car = Octoprime(tires)
        self.assertTrue(car.needs_service())