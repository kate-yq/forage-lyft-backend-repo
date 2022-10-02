from abc import ABC
from datetime import datetime

from car import Car


class Battery(Car, ABC):
    def __init__(self, last_service_date, battery_type):
        super().__init__(last_service_date)
        valid = {"spindler", "nubbin"}
        if battery_type in valid:
            self.battery_type = battery_type
        else: 
            raise ValueError("results: engine type must be one of %r." % valid)

    def battery_should_be_serviced(self):
        if self.engine_type == "spindler":
            service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 2)
            if service_threshold_date < datetime.today().date() or self.engine_should_be_serviced():
                return True
            else:
                return False
        elif self.engine_type == "nubbin":
            service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 4)
            if service_threshold_date < datetime.today().date() or self.engine_should_be_serviced():
                return True
            else:
                return False