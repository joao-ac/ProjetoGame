from code.Const import ENTITY_SPEED
from code.Entity import Entity
import pygame.transform


class PlayerShot(Entity):

    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        # Rotate the sprite 90 degrees counterclockwise to point upward
        self.surf = pygame.transform.rotate(self.surf, 90)

    def move(self):
        self.rect.centery -= ENTITY_SPEED[self.name]
        if self.rect.bottom <= 0:
            self.rect.top = 0
