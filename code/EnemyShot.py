from code.Const import ENTITY_SPEED, WIN_HEIGHT
from code.Entity import Entity


class EnemyShot(Entity):

    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    def move(self):
        self.rect.centery += ENTITY_SPEED[self.name]
        if self.rect.top >= WIN_HEIGHT:
            self.health = 0  # Set health to 0 when reaching the bottom
            self.rect.bottom = 0  # Keep the position at the bottom for visual consistency
