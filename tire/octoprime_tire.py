from tire.tire import Tire


class OctoprimeTire(Tire):
    def __init__(self, array4):
        self.array4 = array4

    def needs_service(self):
        sum = 0
        for a in self.array4:
            sum = sum + a
        if sum >= 3:
            return True
        else: 
            return False