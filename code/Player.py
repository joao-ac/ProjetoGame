#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

from code.Const import ENTITY_SPEED, WIN_WIDTH, PLAYER_KEY_LEFT, PLAYER_KEY_RIGHT, PLAYER_KEY_SHOOT, ENTITY_SHOT_DELAY
from code.Entity import Entity
from code.PlayerShot import PlayerShot


class Player(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.shot_delay = 0  # Start with delay at 0
        self.initial_y = position[1]  # Store initial Y position

    def move(self):
        pressed_key = pygame.key.get_pressed()
        # Only allow horizontal movement
        if pressed_key[PLAYER_KEY_LEFT[self.name]] and self.rect.left > 0:
            self.rect.centerx -= ENTITY_SPEED[self.name]
        elif pressed_key[PLAYER_KEY_RIGHT[self.name]] and self.rect.right < WIN_WIDTH:
            self.rect.centerx += ENTITY_SPEED[self.name]
        # Keep Y position fixed
        self.rect.centery = self.initial_y

    def shoot(self):
        pressed_key = pygame.key.get_pressed()
        if pressed_key[PLAYER_KEY_SHOOT[self.name]]:
            if self.shot_delay <= 0:
                self.shot_delay = ENTITY_SHOT_DELAY[self.name]
                # Create two bullets, one from left and one from right
                left_bullet = PlayerShot(name=f'{self.name}Shot', position=(self.rect.centerx - 25, self.rect.centery))
                right_bullet = PlayerShot(name=f'{self.name}Shot', position=(self.rect.centerx + 15, self.rect.centery))
                return [left_bullet, right_bullet]
        self.shot_delay -= 1
        return None
