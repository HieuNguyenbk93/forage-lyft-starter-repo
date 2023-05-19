from tier.tier import Tier

class CarriganTier(Tier):
    def __init__(self, tire_wear_arr):
        self.tire_wear_arr = tire_wear_arr

    def needs_service(self):
        return self.tire_wear_arr[0] <= 0.9 or self.tire_wear_arr[1] <= 0.9 or self.tire_wear_arr[2] <= 0.9 or self.tire_wear_arr[3] <= 0.9