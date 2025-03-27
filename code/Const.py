# C
import pygame

COLOR_ORANGE = (255, 165, 0)
COLOR_GREEN = (0, 255, 0)
COLOR_BLUE = (0, 0, 255)
COLOR_YELLOW = (255, 255, 0)
COLOR_MAGENTA = (255, 0, 255)
COLOR_RED = (255, 0, 0)
COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)

# E
EVENT_ENEMY = pygame.USEREVENT + 1
ENTITY_HEALTH = {
    'Level1Bg0': 999,
    'Level1Bg1': 999,
    'Level1Bg2': 999,
    'Level1Bg3': 999,
    'Level1Bg4': 999,
    'Level1Bg5': 999,
    'Level1Bg6': 999,
    'Player1': 300,
    'Player1Shot': 300,
    'Player2': 300,
    'Player2Shot': 300,
    'Enemy1': 50,
    'Enemy1Shot': 50,
    'Enemy2': 60,
    'Enemy2Shot': 60
}
ENTITY_DAMAGE = 20
ENTITY_SCORE = 0
ENTITY_SPEED = {
    'Level1Bg0': 0,
    'Level1Bg1': 1,
    'Level1Bg2': 2,
    'Level1Bg3': 3,
    'Level1Bg4': 4,
    'Level1Bg5': 5,
    'Level1Bg6': 6,
    'Player1': 2,
    'Player1Shot' : 4,
    'Player2': 2,
    'Player2Shot': 4,
    'Enemy1': 1,
    'Enemy1Shot': 3,
    'Enemy2': 1,
    'Enemy2Shot': 3
}

ENTITY_SHOT_DELAY = {
    'Player1': 30,
    'Player2': 30,
    'Enemy1': 60,
    'Enemy2': 60
}

# M
MENU_OPTION = ('NEW GAME 1P',
               'NEW GAME 2P- COOPERATIVE',
               'NEW GAME 2P- COMPETITIVE',
               'SCORE',
               'EXIT')

# P
PLAYER_KEY_UP = {
    'Player1': pygame.K_UP,
    'Player2': pygame.K_w
}
PLAYER_KEY_DOWN = {
    'Player1': pygame.K_DOWN,
    'Player2': pygame.K_s
}
PLAYER_KEY_LEFT = {
    'Player1': pygame.K_LEFT,
    'Player2': pygame.K_a
}
PLAYER_KEY_RIGHT = {
    'Player1': pygame.K_RIGHT,
    'Player2': pygame.K_d
}
PLAYER_KEY_SHOOT = {
    'Player1': pygame.K_SPACE,
    'Player2': pygame.K_LCTRL
}

# S
SPAWN_TIME = 1000

# W
WIN_WIDTH = 576
WIN_HEIGHT = 324
