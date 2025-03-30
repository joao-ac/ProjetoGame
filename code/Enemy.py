#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
from code.Const import ENTITY_SPEED, ENTITY_SHOT_DELAY, WIN_HEIGHT, WIN_WIDTH
from code.EnemyShot import EnemyShot
from code.Entity import Entity
import pygame.transform


class Enemy(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.shot_delay = ENTITY_SHOT_DELAY[self.name]
        self.horizontal_direction = random.choice([-1, 1])  # Random initial direction
        self.base_horizontal_speed = ENTITY_SPEED[self.name] * 1.2
        self.base_vertical_speed = ENTITY_SPEED[self.name] * 0.8
        self.horizontal_speed = self.base_horizontal_speed * random.uniform(0.8, 1.2)  # Random speed variation
        self.vertical_speed = self.base_vertical_speed * random.uniform(0.8, 1.2)  # Random speed variation
        self.zigzag_counter = random.randint(0, 60)  # Random initial counter
        self.zigzag_frequency = random.randint(60, 120)  # Random frequency between 60-120 frames (1-2 seconds)
        self.random_change_chance = 0.005  # Reduced to 0.5% chance to change direction randomly each frame
        # Initialize with random shot delay
        self.shot_delay = random.randint(90, 150)  # Random delay between 1.5-2.5 seconds at 60 FPS
        self.original_surf = self.surf.copy()  # Store original sprite
        self.angle = 180  # Start pointing downward

    def move(self):
        # Vertical movement with slight random variation
        self.rect.centery += self.vertical_speed
        if self.rect.top >= WIN_HEIGHT:
            self.rect.bottom = 0
            # Randomize speeds when respawning
            self.horizontal_speed = self.base_horizontal_speed * random.uniform(0.8, 1.2)
            self.vertical_speed = self.base_vertical_speed * random.uniform(0.8, 1.2)
            # New random shot delay when respawning
            self.shot_delay = random.randint(90, 150)
            
        # Random direction changes (less frequent)
        if random.random() < self.random_change_chance:
            self.horizontal_direction *= -1
            
        # Zigzag pattern with longer random timing
        self.zigzag_counter += 1
        if self.zigzag_counter >= self.zigzag_frequency:
            self.horizontal_direction *= -1
            self.zigzag_counter = 0
            self.zigzag_frequency = random.randint(60, 120)  # New random frequency
            
        # Horizontal movement
        self.rect.centerx += self.horizontal_speed * self.horizontal_direction
        
        # Bounce off screen edges
        if self.rect.right >= WIN_WIDTH:
            self.horizontal_direction = -1
        elif self.rect.left <= 0:
            self.horizontal_direction = 1
            
        # Update rotation based on movement direction
        if self.horizontal_direction > 0:
            self.angle = 90  # Point downward-right
        else:
            self.angle = 90  # Point downward-left
            
        # Rotate the sprite
        self.surf = pygame.transform.rotate(self.original_surf, self.angle)
        # Update rect to match new sprite size
        self.rect = self.surf.get_rect(center=self.rect.center)

    def shoot(self):
        self.shot_delay -= 1
        if self.shot_delay == 0:
            # Set new random delay after shooting
            self.shot_delay = random.randint(90, 150)
            return EnemyShot(name=f'{self.name}Shot', position=(self.rect.centerx, self.rect.centery))