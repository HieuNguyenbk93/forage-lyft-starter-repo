from tier.tier import Tier

class OctoprimeTier(Tier):
    def __init__(self, tire_wear_arr):
        self.tire_wear_arr = tire_wear_arr

    def needs_service(self):
        total_wear = 0
        for x in self.tire_wear_arr:
            total_wear = total_wear + x
        return total_wear <= 3