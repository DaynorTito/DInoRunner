from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import POISON

class Poison(Obstacle):
    def __init__(self):
        self.image = POISON
        super().__init__(self.image ,0 ,"poison")