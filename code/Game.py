import pygame

from code.Menu import Menu
from code.Const import WIN_WIDTH, WIN_HEIGHT

class Game:
    def __init__(self):
        self.window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        pygame.display.set_caption('Game')
        pygame.init()

    def run(self, ):

        while True:
            menu = Menu(self.window)
            menu.run()
            pass

        # while True:
        #     for event in pygame.event.get():
        #         if event.type == pygame.QUIT:
        #             pygame.quit()
        #             quit()
