from criteria.engine import Engine
from criteria.battery import Battery


class Palindrome(Engine, Battery):
    def __init__(self, last_service_date, warning_light_is_on):
        self.engine_type = "sternman"
        self.battery_type = "spindler"
        self.last_service_date = last_service_date

    def needs_service(self):
        if self.battery_should_be_serviced() or self.engine_should_be_serviced():
            return True
        else:
            return False