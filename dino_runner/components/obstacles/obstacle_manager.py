#obstacle_manager.py
import random, pygame
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.bird import Bird
from dino_runner.components.obstacles.speed_pill import SpeedPill
from dino_runner.components.obstacles.poison import Poison
from dino_runner.utils.constants import LARGE_CACTUS, SMALL_CACTUS, BIRD

class ObstacleManager:
    def __init__(self):
        self.obstacles = []
        
    def update(self, game):
        if len(self.obstacles)==0:
            cactus_size = random.randint(0,100)
            if 0<=cactus_size<=20:
                smallCactus = Cactus(SMALL_CACTUS)
                smallCactus.rect.y = 325
                self.obstacles.append(smallCactus)
            elif 21<=cactus_size<=40:
                pos_bird = [235,272,327]
                pos = random.randint(0,2)
                bird = Bird(BIRD)
                bird.rect.y = pos_bird[pos]
                self.obstacles.append(bird)
            elif 41<=cactus_size<=55:
                pill_blue = SpeedPill()
                pill_blue.rect.y = 327
                self.obstacles.append(pill_blue)
            elif 56<=cactus_size<=74:
                poison = Poison()
                poison.rect.y = 327
                self.obstacles.append(poison)
            else:
                largeCactus = Cactus(LARGE_CACTUS)
                largeCactus.rect.y = 305
                self.obstacles.append(largeCactus)

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed,self.obstacles)
            if (game.player.dino_rect.colliderect(obstacle.rect) and not(game.player.shield) and not(game.player.hammer) and obstacle.name!="pill" and obstacle.name !="poison") or (game.player.dino_rect.colliderect(obstacle.rect) and game.player.hammer and obstacle.name == "bird"):
                game.player_heart_manager.reduce_heart()
                if game.player_heart_manager.heart_count > 0:
                    self.obstacles.pop()
                else:
                    pygame.time.delay(1000)
                    game.sum_death()
                    self.obstacles.remove(obstacle)
                    game.close()
                    game.sound_game.stop()
                    game.show_sub_menu()
                    break
            elif game.player.hammer and game.player.dino_rect.colliderect(obstacle.rect) and obstacle.name == "cactus":
                self.obstacles.pop()
            elif game.player.dino_rect.colliderect(obstacle.rect) and obstacle.name == "pill" and game.player.pill==False and game.player.velocity ==False and game.player.shield==False:
                obstacle.start_time = pygame.time.get_ticks()
                game.player.pill = True
                obstacle.start_time = pygame.time.get_ticks()
                if game.player.pill: game.player.pill_time_up = obstacle.start_time + (random.randint(5,8)*1000)
                self.obstacles.pop()
            elif game.player.dino_rect.colliderect(obstacle.rect) and obstacle.name == "poison" and game.player.poison == False and game.player.velocity ==False and game.player.shield==False:
                obstacle.start_time = pygame.time.get_ticks()
                game.player.poison = True
                obstacle.start_time = pygame.time.get_ticks()
                if game.player.poison: game.player.poison_time_up = obstacle.start_time + (random.randint(5,8)*1000)
                self.obstacles.pop()
    def draw(self,screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)