from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import PILL_BLUE
import random
class SpeedPill(Obstacle):
    def __init__(self):
        self.image = PILL_BLUE
        super().__init__(self.image, 0, "pill")

    