from abc import ABC

from car import Car


class Engine(Car, ABC):
    def __init__(self, engine_type, last_service_date, current_mileage = 0, last_service_mileage = 0, warning_light_is_on = False):
        super().__init__(last_service_date)
        valid = {"capulet", "sternman", "willoughby"}
        if engine_type in valid:
            self.engine_type = engine_type
        else: 
            raise ValueError("results: engine type must be one of %r." % valid)
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage
        self.warning_light_is_on = warning_light_is_on

    def engine_should_be_serviced(self):
        if self.engine_type == "capulet":
            return self.current_mileage - self.last_service_mileage > 30000
        elif self.engine_type == "willoughby":
            return self.current_mileage - self.last_service_mileage > 60000
        elif self.engine_type == "sternman":
            if self.warning_light_is_on:
                return True
            else:
                return False