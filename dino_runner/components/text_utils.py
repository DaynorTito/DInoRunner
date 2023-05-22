import pygame
from dino_runner.utils.constants import SCREEN_HEIGHT, SCREEN_WIDTH

FONT_STYLE = 'freesansbold.ttf'
text_black_color = (0,0,0) # rgb
def get_centered_message(message, width = SCREEN_WIDTH//2, height = SCREEN_HEIGHT//2):
    font = pygame.font.Font(FONT_STYLE, 24)
    text = font.render(message,True,text_black_color)
    text_rect = text.get_rect()
    text_rect.center=(width,height)
    return (text, text_rect)

def get_score_element(points):
    font = pygame.font.Font(FONT_STYLE, 22)
    text = font.render("Points: "+str(points),True,text_black_color)
    text_rect = text.get_rect()
    text_rect.center= (1000,50)
    return (text, text_rect)