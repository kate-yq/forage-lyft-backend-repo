import unittest

from tire.carrigan_tire import CarriganTire
from tire.octoprime_tire import OctoprimeTire


class TestCarriganTire(unittest.TestCase):
    def test_needs_service_true(self):
        array4 = [0.9, 0.8, 0.8, 0.7]
        tire = CarriganTire(array4)
        self.assertTrue(tire.needs_service())

    def test_needs_service_false(self):
        array4 = [0.8, 0.8, 0.8, 0.7]
        tire = CarriganTire(array4)
        self.assertFalse(tire.needs_service())

class TestOctoprimeTire(unittest.TestCase):
    def test_needs_service_true(self):
        array4 = [0.8, 0.8, 0.7, 0.7]
        tire = OctoprimeTire(array4)
        self.assertTrue(tire.needs_service())

    def test_needs_service_false(self):
        array4 = [0.8, 0.8, 0.6, 0.7]
        tire = OctoprimeTire(array4)
        self.assertFalse(tire.needs_service())


if __name__ == '__main__':
    unittest.main()
