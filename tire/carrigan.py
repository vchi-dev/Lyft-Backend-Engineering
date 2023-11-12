from abc import ABC

from tire.tire import Tire

class Carrigan(Tire, ABC):
    def __init__(self, tire_status):
        self.tire_status = tire_status

    def needs_service(self):
        for tire in self.tire_status:
            if tire >= 0.9:
                return True
        return False