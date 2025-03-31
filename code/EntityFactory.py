#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
import os

from code.Background import Background
from code.Const import WIN_WIDTH, WIN_HEIGHT
from code.Enemy import Enemy
from code.Player import Player


class EntityFactory:
    @staticmethod
    def count_background_images(level_name: str) -> int:
        """Count how many background images exist for a given level."""
        count = 0
        while os.path.exists(f'./asset/{level_name}{count}.png'):
            count += 1
        return count

    @staticmethod
    def get_entity(entity_name: str):
        match entity_name:
            case 'Level1Bg':
                list_bg = []
                num_images = EntityFactory.count_background_images('Level1Bg')
                for i in range(num_images):
                    list_bg.append(Background(f'Level1Bg{i}', (0, 0)))
                    list_bg.append(Background(f'Level1Bg{i}', (0, WIN_HEIGHT)))
                return list_bg
            case 'Level2Bg':
                list_bg = []
                num_images = EntityFactory.count_background_images('Level2Bg')
                for i in range(num_images):
                    list_bg.append(Background(f'Level2Bg{i}', (0, 0)))
                    list_bg.append(Background(f'Level2Bg{i}', (0, WIN_HEIGHT)))
                return list_bg
            case 'Level3Bg':
                list_bg = []
                num_images = EntityFactory.count_background_images('Level3Bg')
                for i in range(num_images):
                    list_bg.append(Background(f'Level3Bg{i}', (0, 0)))
                    list_bg.append(Background(f'Level3Bg{i}', (0, WIN_HEIGHT)))
                return list_bg
            case 'Player1':
                return Player('Player1', (WIN_WIDTH / 2 - 30, WIN_HEIGHT - 100))
            case 'Player2':
                return Player('Player2', (WIN_WIDTH / 2 + 30, WIN_HEIGHT - 100))
            case 'Enemy1':
                return Enemy('Enemy1', (0, 0))  # Position will be set by formation
            case 'Enemy2':
                return Enemy('Enemy2', (0, 0))  # Position will be set by formation
