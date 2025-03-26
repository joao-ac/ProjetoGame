import pygame

from code.Level import Level
from code.Menu import Menu
from code.Const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION


class Game:
    def __init__(self):
        self.window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        pygame.display.set_caption('Game')
        pygame.init()

    def run(self, ):

        while True:
            menu = Menu(self.window)
            menu_return = menu.run()

            if menu_return in [MENU_OPTION[0], MENU_OPTION[1], MENU_OPTION[2]]:
                level = Level(self.window, 'Level1', menu_return)
                level_return = level.run()
            elif menu_return == MENU_OPTION[4]:
                pygame.quit()
                quit()
            else:
                pass