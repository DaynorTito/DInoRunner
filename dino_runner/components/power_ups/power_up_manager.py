import random, pygame
from dino_runner.components.power_ups.shield import Shield
from dino_runner.components.power_ups.hammer import Hammer
from dino_runner.components.power_ups.life import Life
from dino_runner.components.power_ups.velocity import Velocity
class PowerUpManager:
    def __init__(self):
        self.power_ups = []
        self.when_appers = 0
        self.points = 0

    def update(self,points,game_speed, player, game):
        self.generate_power_ups(points)
        for powerup in self.power_ups:
            powerup.update(game_speed,self.power_ups)
            if player.dino_rect.colliderect(powerup.rect):
                if powerup.type == "life":
                    if game.player_heart_manager.heart_count<5: game.player_heart_manager.increases_heart()
                else:
                    powerup.start_time = pygame.time.get_ticks()
                    if powerup.type == "shield" and player.shield==False:
                        player.shield = True
                        game.sound_game.stop()
                        player.sound_star.play()
                    elif powerup.type == "hammer": player.hammer = True
                    elif powerup.type == "velocity":
                        player.velocity = True
                        if player.poison: player.poison = False
                    if player.velocity: player.type = "default"
                    else: player.type = powerup.type
                    powerup.start_time = pygame.time.get_ticks()
                    if player.shield: player.shield_time_up = powerup.start_time + (random.randint(5,8)*1000)
                    elif player.hammer: player.hammer_time_up = powerup.start_time + (random.randint(5,8)*1000)
                    elif player.velocity: player.velocity_time_up = powerup.start_time + (random.randint(5,8)*1000)
                self.power_ups.remove(powerup)

    def draw(self, screen):
        for powerup in self.power_ups:
            powerup.draw(screen)

    def generate_power_ups(self, points):
        self.points = points
        if len(self.power_ups)==0:
            if self.when_appers==points:
                self.when_appers = random.randint(self.when_appers + 150, self.when_appers + 500)
                type_power_up = random.randint(0,50)
                if 0<=type_power_up<=10 or type_power_up==0: self.power_ups.append(Shield())
                elif 11<=type_power_up<=20:  self.power_ups.append(Hammer())
                elif 21<=type_power_up<=40: self.power_ups.append(Life())
                else: self.power_ups.append(Velocity())