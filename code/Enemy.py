#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
from code.Const import ENTITY_SPEED, ENTITY_SHOT_DELAY, WIN_HEIGHT, WIN_WIDTH
from code.EnemyShot import EnemyShot
from code.Entity import Entity


class Enemy(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        # Randomize initial shot delay to prevent synchronized shooting
        self.shot_delay = random.randint(0, 300)
        self.horizontal_speed = 2  # Fixed horizontal speed
        self.initial_y = position[1]  # Store initial Y position

    def move(self, formation_direction: int, formation_y: int):
        # Move horizontally with the formation
        self.rect.centerx += self.horizontal_speed * formation_direction
        
        # Apply vertical position based on formation position
        self.rect.centery = self.initial_y + formation_y
        
        # If enemies descend too far, they win
        if self.rect.bottom >= WIN_HEIGHT - 100:
            return True  # Signal game over
            
        return False

    def shoot(self):
        self.shot_delay -= 1
        if self.shot_delay == 0:
            # Set new random delay after shooting
            self.shot_delay = random.randint(180, 300)  # Much longer delay between shots
            return EnemyShot(name=f'{self.name}Shot', position=(self.rect.centerx, self.rect.centery))
        return None