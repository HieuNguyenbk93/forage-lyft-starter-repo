import unittest
from tier.octoprime_tier import OctoprimeTier

class TestOctoprimeTier(unittest.TestCase):
    def test_needs_service_true(self):
        tire_wear_arr = [1, 1, 1, 1]
        tier = OctoprimeTier(tire_wear_arr)
        self.assertFalse(tier.needs_service())

    def test_needs_service_true(self):
        tire_wear_arr = [1, 1, 1, 0.9]
        tier = OctoprimeTier(tire_wear_arr)
        self.assertTrue(tier.needs_service())