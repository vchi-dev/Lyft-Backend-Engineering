from abc import ABC

from engine.engine import Engine

class NubbinBattery(Engine, ABC):
    def __init__(self, last_service_date, current_date):
        super().__init__(last_service_date)
        self.current_date = current_date
        self.last_service_date = last_service_date

    def needs_service(self):
        return True