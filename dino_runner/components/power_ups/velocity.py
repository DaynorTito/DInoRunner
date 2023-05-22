from dino_runner.components.power_ups.power_up import PowerUp
from dino_runner.utils.constants import VELOCITY, VELOCITY_TYPE
class Velocity(PowerUp):
    def __init__(self):
        self.image = VELOCITY
        self.type = VELOCITY_TYPE
        super().__init__(self.image, self.type)
        