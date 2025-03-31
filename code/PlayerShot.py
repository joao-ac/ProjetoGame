from code.Const import ENTITY_SPEED
from code.Entity import Entity


class PlayerShot(Entity):

    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    def move(self):
        self.rect.centery -= ENTITY_SPEED[self.name]
        if self.rect.bottom <= 0:
            self.health = 0  # Set health to 0 when reaching the top
