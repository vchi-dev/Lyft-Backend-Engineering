from battery.battery import Battery
from engine.engine import Engine
from serviceable import Serviceable


class Car(Serviceable):
    def __init__(self, engine, battery):
        self.engine = Engine()
        self.battery = Battery()

    def needs_service(self) -> bool:
        if (self.engine.needs_service() or self.battery.needs_service()):
            return True;
        else:
            return False;