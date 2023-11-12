from abc import ABC

from tire.tire import Tire

class Octoprime(Tire, ABC):
    def __init__(self, tire_status):
        self.tire_status = tire_status

    def needs_service(self):
        sum = 0
        for tire in self.tire_status:
            sum += tire
        if sum >= 3:
            return True
        else:
            return False
