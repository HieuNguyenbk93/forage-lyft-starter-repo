from abc import ABC

class Tier(ABC):
    def needs_service(self):
        pass