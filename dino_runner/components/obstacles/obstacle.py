from pygame.sprite import Sprite

from dino_runner.utils.constants import SCREEN_WIDTH

#Generic class of obstacles
class Obstacle(Sprite):

    def __init__(self, image, type, name):
        self.image = image
        self.name = name
        self.type = type
        self.start_time = 0
        self.rect = self.image[self.type].get_rect()
        self.rect.x = SCREEN_WIDTH

    def update(self,game_speed,obstacles):
        self.rect.x -= game_speed
        if self.rect.x < -self.rect.width:
            obstacles.pop()

    def draw(self, screen):
        screen.blit(self.image[self.type],self.rect)






