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
COLOR_CYAN = (0, 255, 255)

# E
EVENT_ENEMY = pygame.USEREVENT + 1
EVENT_TIMEOUT = pygame.USEREVENT + 2
ENTITY_HEALTH = {
    'MenuBg0': 999,
    'MenuBg1': 999,
    'MenuBg2': 999,
    'MenuBg3': 999,
    'MenuBg4': 999,
    'MenuBg5': 999,
    'Level1Bg0': 999,
    'Level1Bg1': 999,
    'Level1Bg2': 999,
    'Level1Bg3': 999,
    'Level1Bg4': 999,
    'Level1Bg5': 999,
    'Level1Bg6': 999,
    'Level2Bg0': 999,
    'Level2Bg1': 999,
    'Level2Bg2': 999,
    'Level2Bg3': 999,
    'Level2Bg4': 999,
    'Level3Bg0': 999,
    'Level3Bg1': 999,
    'Level3Bg2': 999,
    'Level3Bg3': 999,
    'Level3Bg4': 999,
    'Level3Bg5': 999,
    'Player1': 5,
    'Player1Shot': 1,
    'Player2': 5,
    'Player2Shot': 1,
    'Enemy1': 2,
    'Enemy1Shot': 1,
    'Enemy2': 2,
    'Enemy2Shot': 1
}

ENTITY_DAMAGE = {
    'MenuBg0': 0,
    'MenuBg1': 0,
    'MenuBg2': 0,
    'MenuBg3': 0,
    'MenuBg4': 0,
    'MenuBg5': 0,
    'Level1Bg0': 0,
    'Level1Bg1': 0,
    'Level1Bg2': 0,
    'Level1Bg3': 0,
    'Level1Bg4': 0,
    'Level1Bg5': 0,
    'Level1Bg6': 0,
    'Level2Bg0': 0,
    'Level2Bg1': 1,
    'Level2Bg2': 2,
    'Level2Bg3': 3,
    'Level2Bg4': 4,
    'Level3Bg0': 0,
    'Level3Bg1': 0,
    'Level3Bg2': 0,
    'Level3Bg3': 0,
    'Level3Bg4': 0,
    'Level3Bg5': 0,
    'Player1': 1,
    'Player1Shot': 1,
    'Player2': 1,
    'Player2Shot': 1,
    'Enemy1': 1,
    'Enemy1Shot': 1,
    'Enemy2': 1,
    'Enemy2Shot': 1
}

ENTITY_SCORE = {
    'MenuBg0': 0,
    'MenuBg1': 0,
    'MenuBg2': 0,
    'MenuBg3': 0,
    'MenuBg4': 0,
    'MenuBg5': 0,
    'Level1Bg0': 0,
    'Level1Bg1': 0,
    'Level1Bg2': 0,
    'Level1Bg3': 0,
    'Level1Bg4': 0,
    'Level1Bg5': 0,
    'Level1Bg6': 0,
    'Level2Bg0': 0,
    'Level2Bg1': 0,
    'Level2Bg2': 0,
    'Level2Bg3': 0,
    'Level2Bg4': 0,
    'Level3Bg0': 0,
    'Level3Bg1': 0,
    'Level3Bg2': 0,
    'Level3Bg3': 0,
    'Level3Bg4': 0,
    'Level3Bg5': 0,
    'Player1': 0,
    'Player1Shot': 0,
    'Player2': 0,
    'Player2Shot': 0,
    'Enemy1': 10,
    'Enemy1Shot': 0,
    'Enemy2': 10,
    'Enemy2Shot': 0
}
ENTITY_SPEED = {
    'MenuBg0': 0,
    'MenuBg1': 1,
    'MenuBg2': 1,
    'MenuBg3': 2,
    'MenuBg4': 2,
    'MenuBg5': 3,
    'Level1Bg0': 0,
    'Level1Bg1': 1,
    'Level1Bg2': 1,
    'Level1Bg3': 2,
    'Level1Bg4': 2,
    'Level1Bg5': 3,
    'Level1Bg6': 3,
    'Level2Bg0': 0,
    'Level2Bg1': 1,
    'Level2Bg2': 2,
    'Level2Bg3': 3,
    'Level2Bg4': 4,
    'Level3Bg0': 0,
    'Level3Bg1': 2,
    'Level3Bg2': 2,
    'Level3Bg3': 3,
    'Level3Bg4': 3,
    'Level3Bg5': 4,
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
    'Enemy1': 180,
    'Enemy2': 180
}

# M
MENU_OPTION = ('NEW GAME 1P',
               'NEW GAME 2P',
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

# T
TIMEOUT_STEP = 100
TIMEOUT_LEVEL = 30000

# W
WIN_WIDTH = 540
WIN_HEIGHT = 960

# S
SCORE_POS = {
    'Title': (WIN_WIDTH / 2, 80),
    'EnterName': (WIN_WIDTH / 2, 120),
    'Label': (WIN_WIDTH / 2, 140),
    'Name': (WIN_WIDTH / 2, 160),
    0: (WIN_WIDTH / 2, 160),
    1: (WIN_WIDTH / 2, 190),
    2: (WIN_WIDTH / 2, 220),
    3: (WIN_WIDTH / 2, 250),
    4: (WIN_WIDTH / 2, 280),
    5: (WIN_WIDTH / 2, 310),
    6: (WIN_WIDTH / 2, 340),
    7: (WIN_WIDTH / 2, 370),
    8: (WIN_WIDTH / 2, 400),
    9: (WIN_WIDTH / 2, 430)
}