from car import Car
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine
from battery.spindler_battery import SpindlerBattery
from battery.nubbin_battery import NubbinBattery

class CarFactory:
    @staticmethod
    def create_calliope(current_date, last_service_date, current_mileage,
    last_service_mileage):
        #Calliope takes capulet engine and spindler battery
        battery = SpindlerBattery(current_date, last_service_date)
        engine = CapuletEngine(current_mileage, last_service_mileage)
        calliope = Car(engine, spindler)
        return calliope

    @staticmethod
    def create_glissade(current_date, last_service_date, current_mileage,
    last_service_mileage):
        #Glissade takes Willoughby engine and spindler Battery
        spindler = SpindlerBattery(current_date, last_service_date)
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        glissade = Car(engine, spindler)
        return glissade

    @staticmethod
    def create_palindrome(current_date, last_service_date, warning_light_on):
        #panlindrome takes sternman engine and spindler Battery
        spindler = SpindlerBattery(current_date, last_service_date)
        engine = SternmanEngine(warning_light_is_on)
        palindrome = Car(engine, spindler)
        return palindrome

    @staticmethod
    def create_roeschach(current_date, last_service_date, current_mileage, last_service_mileage):
        #Rorschach takes in Willoughby engine and nubbin Battery
        nubbin = NubbinBattery(current_date, last_service_date)
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        roeschach = Car(engine, nubbin)
        return roeschach

    @staticmethod
    def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage):
        #Thovex takes in Capulet Engine and bubbin battery
        nubbin = NubbinBattery(current_date, last_service_date)
        engine = CapuletEngine(current_mileage, last_service_mileage)
        thovex = Car(engine, nubbin)
        return thovex
