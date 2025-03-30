from code.Const import ENTITY_SPEED, WIN_HEIGHT
from code.Entity import Entity
import pygame.transform


class EnemyShot(Entity):

    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        # Rotate the sprite 180 degrees to point downward
        self.surf = pygame.transform.rotate(self.surf, 90)

    def move(self):
        self.rect.centery += ENTITY_SPEED[self.name]
        if self.rect.top >= WIN_HEIGHT:
            self.rect.bottom = 0
