import pygame, sys
from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager
from dino_runner.components.player_hearts.player_heart_manager import PlayerHeartManager
from dino_runner.components.power_ups.power_up_manager import PowerUpManager
from dino_runner.utils.constants import BG,BG_MENU ,ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, PLAY_RECT, OPCION_RECT, QUIT_RECT,SOUND_MENU,SOUND_GAME,SOUND_GAME_OVER
from dino_runner.components import text_utils
from dino_runner.utils.scores_manager import ScoresManager
from dino_runner.utils.button import Button
class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        pygame.mixer.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = 0 #380
        self.player = Dinosaur()
        self.obstacle_manager = ObstacleManager()
        self.player_heart_manager = PlayerHeartManager()
        self.power_up_manager = PowerUpManager()
        self.death_count = 0
        self.points = 0
        self.running = True
        self.speed_buildup = 0
        self.scores_manager = ScoresManager()
        self.sound_menu = SOUND_MENU
        self.sound_game = SOUND_GAME
        self.sound_game_over = SOUND_GAME_OVER
    def execute(self):
        while self.running:
            if not self.playing:
                self.show_menu()
    
    def run(self):
        # Game loop: events - update - draw
        self.restart_elements()
        self.sound_game.play()
        while self.playing:
            self.events()
            self.update()
            self.draw()
        #pygame.quit()
    def restart_elements(self):
        self.playing = True
        self.game_speed = 20
        self.player = Dinosaur()
        self.obstacle_manager = ObstacleManager()
        self.player_heart_manager = PlayerHeartManager()
        self.power_up_manager = PowerUpManager()
        self.points = 0
        self.speed_buildup = 0
        self.player_heart_manager = PlayerHeartManager()
        self.scores_manager = ScoresManager()
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.sound_game.stop()
                self.playing = False
    def close(self):
        self.playing=False
    def sum_death(self):
        self.death_count +=1
    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        if self.playing==False:
            self.show_sub_menu()
        else:
            self.obstacle_manager.update(self)
            self.power_up_manager.update(self.points, self.game_speed, self.player, self)

    def draw(self):

        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        
        self.draw_background()
        self.draw_score()
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        self.player_heart_manager.draw(self.screen)
        self.power_up_manager.draw(self.screen)
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed

    def draw_score(self):
        self.points +=1
        if self.player.poison:
            if self.points % 100 == 0: self.player_heart_manager.reduce_heart()
        if self.player.velocity and self.speed_buildup == 0:
            self.speed_buildup = self.game_speed
            self.game_speed = self.game_speed - (self.game_speed*0.6)
        elif self.player.velocity==False and self.speed_buildup != 0:
            self.game_speed = self.speed_buildup
            self.speed_buildup = 0
        elif self.player.pill and self.speed_buildup == 0 and self.player.velocity==False:
            self.speed_buildup = self.game_speed
            self.game_speed = self.game_speed + (self.game_speed*0.4)
        elif self.player.pill==False and self.speed_buildup != 0:
            self.game_speed = self.speed_buildup
            self.speed_buildup = 0

        if self.points % 100 ==0 and self.player.velocity==False and self.player.pill==False:
            self.game_speed +=1
        
        text, text_rect = text_utils.get_score_element(self.points)
        self.player.check_visibility(self.screen,self)
        pygame.draw.rect(self.screen,(255,255,255),text_rect)
        self.screen.blit(text, text_rect)

    def show_menu(self):
        white_color = (85,84,84) # rgb
        self.screen.fill(white_color)
        self.print_elements()
        pygame.display.update()
    def get_font(self,size):
        return pygame.font.Font("freesansbold.ttf", size) 
    
    def show_scores(self):
        list_points = self.scores_manager.best_points()
        while True:
            self.screen.blit(BG_MENU, (0, 0))
            menu_mouse_pos = pygame.mouse.get_pos()
            menu_text = self.get_font(60).render("Best Scores", True, "#555454")
            menu_rect = menu_text.get_rect(center=(SCREEN_WIDTH//2, 85))
            quit_button = Button(image=QUIT_RECT, pos=(SCREEN_WIDTH//2, 460), text_input="Back", font=self.get_font(40), base_color="#d7fcd4", hovering_color="White")
            self.screen.blit(menu_text, menu_rect)
            for i in range(len(list_points)):
                if i==4: break
                point_1 = self.get_font(48).render(str(i+1)+".- "+str(list_points[i])+" points",True, "#555454")
                ponit_1rect = point_1.get_rect(center=(SCREEN_WIDTH//2, 170+(i*55)))
                self.screen.blit(point_1, ponit_1rect)
            for button in [quit_button]:
                button.changeColor(menu_mouse_pos)
                button.update(self.screen)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.playing = False
                    self.running = False
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if quit_button.checkForInput(menu_mouse_pos):
                        self.sound_menu.stop()
                        self.show_main_menu()
            pygame.display.update()

    def show_main_menu(self):
        self.sound_menu.play(3)
        while True:
            self.screen.blit(BG_MENU, (0, 0))
            menu_mouse_pos = pygame.mouse.get_pos()
            menu_text = self.get_font(60).render("Welcome Dino Runer", True, "#555454")
            menu_rect = menu_text.get_rect(center=(SCREEN_WIDTH//2, 85))
            play_button = Button(image=PLAY_RECT , pos=(SCREEN_WIDTH//2, 220), text_input="PLAY", font=self.get_font(40), base_color="#d7fcd4", hovering_color="White")
            options_button = Button(image=OPCION_RECT, pos=(SCREEN_WIDTH//2, 320), text_input="SCORES", font=self.get_font(40), base_color="#d7fcd4", hovering_color="White")
            quit_button = Button(image=QUIT_RECT, pos=(SCREEN_WIDTH//2, 420), text_input="QUIT", font=self.get_font(40), base_color="#d7fcd4", hovering_color="White")
            self.screen.blit(menu_text, menu_rect)
            for button in [play_button, options_button, quit_button]:
                button.changeColor(menu_mouse_pos)
                button.update(self.screen)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.playing = False
                    self.running = False
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if play_button.checkForInput(menu_mouse_pos):
                        self.sound_menu.stop()
                        self.run()
                    if options_button.checkForInput(menu_mouse_pos):
                        self.show_scores()
                    if quit_button.checkForInput(menu_mouse_pos):
                        self.playing = False
                        self.running = False
                        self.sound_menu.stop()
                        pygame.quit()
                        sys.exit()
            pygame.display.update()
    def show_sub_menu(self):
        pas = 0
        self.sound_game_over.play()
        while True:
            self.screen.blit(BG_MENU, (0, 0))
            menu_mouse_pos = pygame.mouse.get_pos()
            menu_text = self.get_font(60).render("GAME OVER :(", True, "#555454")
            points_text = self.get_font(40).render("You got "+str(self.points)+" points in the game", True, "#555454")
            if pas == 0: self.scores_manager.add_point(self.points)
            pas+=1
            menu_rect = menu_text.get_rect(center=(SCREEN_WIDTH//2, 85))
            points_rect = points_text.get_rect(center=(SCREEN_WIDTH//2, 170))
            play_button = Button(image=PLAY_RECT , pos=(SCREEN_WIDTH//2, 270), text_input="RESTART..?", font=self.get_font(40), base_color="#d7fcd4", hovering_color="White")
            options_button = Button(image=OPCION_RECT, pos=(SCREEN_WIDTH//2, 370), text_input="MAIN MENU", font=self.get_font(40), base_color="#d7fcd4", hovering_color="White")
            
            self.screen.blit(menu_text, menu_rect)
            self.screen.blit(points_text, points_rect)
            for button in [play_button, options_button]:
                button.changeColor(menu_mouse_pos)
                button.update(self.screen)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if play_button.checkForInput(menu_mouse_pos):
                        self.run()
                    elif options_button.checkForInput(menu_mouse_pos):
                        self.show_main_menu()
            pygame.display.update()
    def print_elements(self):
        if self.death_count ==0:
            self.show_main_menu()
        elif self.death_count > 0:
            self.show_sub_menu()
    def handle_key_events_on_menu(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False
                pygame.display.quit()
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                self.run()  
    