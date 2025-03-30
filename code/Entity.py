#!/usr/bin/python
# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod

import pygame.image
import pygame.transform

from code.Const import ENTITY_HEALTH, ENTITY_DAMAGE, ENTITY_SCORE, WIN_WIDTH, WIN_HEIGHT


class Entity(ABC):
    def __init__(self, name: str, position: tuple):
        self.name = name
        # Load the original image
        original_surf = pygame.image.load('./asset/' + name + '.png').convert_alpha()
        
        # Scale the image based on entity type
        if name.startswith('Level'):
            # For background images, scale to window height
            scale_factor = WIN_HEIGHT / original_surf.get_height()
            new_width = int(original_surf.get_width() * scale_factor)
            new_height = int(original_surf.get_height() * scale_factor)
            self.surf = pygame.transform.scale(original_surf, (new_width, new_height))
        elif 'Shot' in name:
            # For shots, make them much smaller
            scale_factor = min(WIN_WIDTH / original_surf.get_width(), WIN_HEIGHT / original_surf.get_height()) * 0.03
            new_width = int(original_surf.get_width() * scale_factor)
            new_height = int(original_surf.get_height() * scale_factor)
            self.surf = pygame.transform.scale(original_surf, (new_width, new_height))
        else:
            # For other entities (players, enemies), maintain aspect ratio but scale to a reasonable size
            scale_factor = min(WIN_WIDTH / original_surf.get_width(), WIN_HEIGHT / original_surf.get_height()) * 0.1
            new_width = int(original_surf.get_width() * scale_factor)
            new_height = int(original_surf.get_height() * scale_factor)
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
