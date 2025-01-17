from battery.battery import Battery

class SpindlerBattery(Battery):
    def __init__(self, current_date, last_service_date):
        self.__current_date = current_date
        self.__last_service_date = __last_service_date

    def needs_service():
        return self.__current_date -self.__last_service_date == 3
