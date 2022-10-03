from tire.tire import Tire


class CarriganTire(Tire):
    def __init__(self, array4):
        self.array4 = array4

    def needs_service(self):
        for a in self.array4:
            if a>=0.9:
                return True
        return False