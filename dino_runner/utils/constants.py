import pygame
import os

# Global Constants
TITLE = "Chrome Dino Runner"
pygame.mixer.init()
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
FPS = 30
IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")
FILE_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")
FILE_1 = os.path.join(IMG_DIR, "Files/arch1.txt")
FILE_2 = os.path.join(IMG_DIR, "Files/arch2.txt")
# Assets Constants
ICON = pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoWallpaper.png"))

RUNNING = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun2.png")),
]

RUNNING_SHIELD = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun1Shield.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun2Shield.png")),
]

RUNNING_HAMMER = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun1Hammer.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun2Hammer1.png")),
]

JUMPING = pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoJump.png"))
JUMPING_SHIELD = pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoJumpShield.png"))
JUMPING_HAMMER = pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoJumpHammer.png"))

DUCKING = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck2.png")),
]

DUCKING_SHIELD = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1Shield.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck2Shield.png")),
]

DUCKING_HAMMER = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1Hammer.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck2Hammer.png")),
]

SMALL_CACTUS = [
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/SmallCactus1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/SmallCactus2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/SmallCactus3.png")),
]
LARGE_CACTUS = [
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus3.png")),
]

BIRD = [
    pygame.image.load(os.path.join(IMG_DIR, "Bird/Bird1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Bird/Bird2.png")),
]

CLOUD = pygame.image.load(os.path.join(IMG_DIR, 'Other/Cloud.png'))
SHIELD = pygame.image.load(os.path.join(IMG_DIR, 'Other/shield.png'))
HAMMER = pygame.image.load(os.path.join(IMG_DIR, 'Other/hammer.png'))
VELOCITY = pygame.image.load(os.path.join(IMG_DIR, 'Other/velocity.png'))
PILL_BLUE = [pygame.image.load(os.path.join(IMG_DIR, 'Other/bluePill.png'))]
POISON = [pygame.image.load(os.path.join(IMG_DIR, 'Other/poison.png'))]
BG = pygame.image.load(os.path.join(IMG_DIR, 'Menu/back9.png'))
BG_MENU = pygame.image.load(os.path.join(IMG_DIR, 'Menu/back_menu.png'))
PLAY_RECT = pygame.image.load(os.path.join(IMG_DIR, 'Menu/Play Rect.png'))
OPCION_RECT = pygame.image.load(os.path.join(IMG_DIR, 'Menu/Options Rect.png'))
QUIT_RECT=pygame.image.load(os.path.join(IMG_DIR, 'Menu/Quit Rect.png')) 

HEART = pygame.image.load(os.path.join(IMG_DIR, 'Other/SmallHeart.png'))

DEFAULT_TYPE = "default"
VELOCITY_TYPE = "velocity"
SHIELD_TYPE = "shield"
HAMMER_TYPE = "hammer"
LIFE_TYPE = "life"
HEART_COUNT = 5

SOUND_JUMP = pygame.mixer.Sound(os.path.join(IMG_DIR, 'Sounds/jump.mp3'))
SOUND_GAME = pygame.mixer.Sound(os.path.join(IMG_DIR, 'Sounds/game.mp3'))
SOUND_STAR = pygame.mixer.Sound(os.path.join(IMG_DIR, 'Sounds/star.mp3'))
SOUND_MENU = pygame.mixer.Sound(os.path.join(IMG_DIR, 'Sounds/menu.mp3'))
SOUND_GAME_OVER = pygame.mixer.Sound(os.path.join(IMG_DIR, 'Sounds/game_over.wav'))
#SOUND_OBSTACLE = pygame.mixer.Sound(os.path.join(IMG_DIR, 'Sounds/obstacle.mp3'))