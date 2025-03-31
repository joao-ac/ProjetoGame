#!/usr/bin/python
# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod

import pygame.image
import pygame.transform

from code.Const import ENTITY_HEALTH, ENTITY_DAMAGE, ENTITY_SCORE, WIN_WIDTH, WIN_HEIGHT

# Scaling factors for different entity types
SCALE_FACTORS = {
    'background': 1.0,  # Backgrounds scale to window height
    'player': 0.05,     # Players are 15% of window height
    'enemy': 0.05,      # Enemies are 12% of window height
    'shot': 0.018        # Shots are 5% of window height
}

class Entity(ABC):
    def __init__(self, name: str, position: tuple):
        self.name = name
        # Load the original image
        original_surf = pygame.image.load('./asset/' + name + '.png').convert_alpha()
        
        # Determine entity type and apply appropriate scaling
        if name.startswith('Level'):
            # Background images scale to window height
            scale_factor = WIN_HEIGHT / original_surf.get_height()
            new_width = int(original_surf.get_width() * scale_factor)
            new_height = int(original_surf.get_height() * scale_factor)
            self.surf = pygame.transform.scale(original_surf, (new_width, new_height))
        else:
            # For other entities, scale based on window height
            base_scale = WIN_HEIGHT / original_surf.get_height()
            
            if 'Shot' in name:
                scale = base_scale * SCALE_FACTORS['shot']
            elif name.startswith('Player'):
                scale = base_scale * SCALE_FACTORS['player']
            elif name.startswith('Enemy'):
                scale = base_scale * SCALE_FACTORS['enemy']
            else:
                scale = base_scale * SCALE_FACTORS['background']
                
            new_width = int(original_surf.get_width() * scale)
            new_height = int(original_surf.get_height() * scale)
            self.surf = pygame.transform.scale(original_surf, (new_width, new_height))
            
        self.rect = self.surf.get_rect(left=position[0], top=position[1])
        self.speed = 0
        self.health = ENTITY_HEALTH[self.name]
        self.damage = ENTITY_DAMAGE[self.name]
        self.last_dmg = 'None'
        self.score = ENTITY_SCORE[self.name]

    @abstractmethod
    def move(self):
        pass
