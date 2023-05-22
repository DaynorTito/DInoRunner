from dino_runner.components.obstacles.obstacle import Obstacle
import random
class Bird(Obstacle):
    def __init__(self, image):
        super().__init__(image, 0,"bird")
        self.rect.y = 0
        self.step_fly = 0

    def draw(self, screen):
        if self.step_fly >= 10: self.step_fly = 0
        screen.blit(self.image[self.step_fly//5], self.rect)
        self.step_fly+=1
