#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.Const import WIN_WIDTH, WIN_HEIGHT, ENTITY_SPEED
from code.Entity import Entity


class Background(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    def move(self):
        # For menu backgrounds, move left
        if self.name.startswith('MenuBg'):
            self.rect.x -= ENTITY_SPEED[self.name]
            
            # Reset position when background moves off screen to the left
            if self.rect.right < 0:
                self.rect.left = WIN_WIDTH
        else:
            # For level backgrounds, move down
            self.rect.y += ENTITY_SPEED[self.name]
            if self.rect.top >= WIN_HEIGHT:
                self.rect.bottom = 0
