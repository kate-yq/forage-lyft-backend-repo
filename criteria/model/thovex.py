from criteria.engine import Engine
from criteria.battery import Battery


class Thovex(Engine, Battery):
    def __init__(self, last_service_date, current_mileage, last_service_mileage):
        self.engine_type = "capulet"
        self.battery_type = "nubbin"
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage
        self.last_service_date = last_service_date

    def needs_service(self):
        if self.battery_should_be_serviced() or self.engine_should_be_serviced():
            return True
        else:
            return False
