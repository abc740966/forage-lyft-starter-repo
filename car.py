from engine import Engine:
from battery import Battery:

class Serviceable(Car):

    def needs_service(self, engine, battery):
        return Car(engine, battery)

class Car(Engine, Battery):
    def __init__(self, engine, battery):
        self.__engine = Engine()
        self.__battery = Battery()

    def needs_service(self):
        return self.engine.needs_service()
        or self.battery.needs_service()
