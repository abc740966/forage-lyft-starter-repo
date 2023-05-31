from tires import Tires

class Octoprime_tires(Tires):
    """Carrigan tires require service onlyk when one or more of the values wear
    array is greater than or equal to 0.9"""

    def __init__(self, tire_wear_arr: list):
        self.tire_wear_arr = tire_wear_arr

    def needs_service(self, tire_wear_arr):
        return sum(tire_wear_arr) >= 3.0
