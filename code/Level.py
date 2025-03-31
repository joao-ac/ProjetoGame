#!/usr/bin/python
# -*- coding: utf-8 -*-
import random

import pygame
from pygame import KEYDOWN, Surface, Rect
from pygame.font import Font

from code.Const import COLOR_WHITE, WIN_HEIGHT, MENU_OPTION, EVENT_ENEMY, SPAWN_TIME, COLOR_GREEN, COLOR_CYAN, \
    EVENT_TIMEOUT, TIMEOUT_STEP, TIMEOUT_LEVEL, WIN_WIDTH, COLOR_RED, COLOR_BLUE
from code.Enemy import Enemy
from code.Entity import Entity
from code.EntityFactory import EntityFactory
from code.EntityMediator import EntityMediator
from code.Player import Player


class Level:
    def __init__(self, window: Surface, name: str, game_mode, player_score: list[int]):
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity(self.name + 'Bg'))
        
        # Set player positions based on game mode
        if game_mode == MENU_OPTION[0]:  # 1 Player mode
            player = EntityFactory.get_entity('Player1')
            player.score = player_score[0]
            player.rect.centerx = WIN_WIDTH // 2  # Center horizontally
            player.rect.bottom = WIN_HEIGHT - 50  # Near bottom
            self.entity_list.append(player)
        else:  # Cooperative 2 Player mode
            # Player 1 (right side)
            player1 = EntityFactory.get_entity('Player1')
            player1.score = player_score[0]  # Both players share the same score
            player1.rect.right = WIN_WIDTH - 50  # Right side
            player1.rect.bottom = WIN_HEIGHT - 50  # Near bottom
            self.entity_list.append(player1)
            
            # Player 2 (left side)
            player2 = EntityFactory.get_entity('Player2')
            player2.score = player_score[0]  # Both players share the same score
            player2.rect.left = 50  # Left side
            player2.rect.bottom = WIN_HEIGHT - 50  # Near bottom
            self.entity_list.append(player2)

        self.formation_y = 0  # Track formation Y position

    def count_enemies(self) -> int:
        return sum(1 for ent in self.entity_list if isinstance(ent, Enemy))

    def run(self, player_score: list[int]):
        # Load music based on level
        if self.name == 'Level2':
            pygame.mixer_music.load(f'./asset/{self.name}.mp3')
        else:
            pygame.mixer_music.load(f'./asset/{self.name}.wav')
        pygame.mixer_music.set_volume(1.0)
        pygame.mixer_music.play(-1)
        clock = pygame.time.Clock()
        
        # Create initial enemy formation
        self.create_enemy_formation()
        self.formation_y = 0  # Reset formation Y position
        formation_direction = 1  # 1 for right, -1 for left
        
        while True:
            clock.tick(60)
            
            # First, handle enemy formation movement
            enemies = [e for e in self.entity_list if isinstance(e, Enemy)]
            if enemies:
                formation_rightmost_x = max(e.rect.right for e in enemies)
                formation_leftmost_x = min(e.rect.left for e in enemies)
                game_over = False
                
                # Check if formation needs to change direction and descend
                if formation_direction > 0 and formation_rightmost_x >= WIN_WIDTH - 20:
                    formation_direction = -1
                    self.formation_y += 5  # Move formation down
                elif formation_direction < 0 and formation_leftmost_x <= 20:
                    formation_direction = 1
                    self.formation_y += 5  # Move formation down
                
                # Move all enemies
                for enemy in enemies:
                    enemy.move(formation_direction, self.formation_y)
                    if enemy.rect.bottom >= WIN_HEIGHT - 100:  # Check if enemies reached bottom
                        game_over = True
                        break
                
                if game_over:
                    return False  # Game over if enemies reach bottom
            
            # Then handle all other entity movement and rendering
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                if not isinstance(ent, Enemy):  # Skip enemy movement as it's handled above
                    ent.move()
                    
                if isinstance(ent, (Player, Enemy)):
                    shoot = ent.shoot()
                    if shoot is not None:
                        if isinstance(shoot, list):
                            self.entity_list.extend(shoot)
                        else:
                            self.entity_list.append(shoot)
                if ent.name == 'Player1':
                    self.draw_score(ent, (20, 20), COLOR_BLUE)
                    if self.game_mode == MENU_OPTION[0]:  # 1 Player mode
                        self.draw_health_bar(ent, (WIN_WIDTH//2 - 75, WIN_HEIGHT - 60), COLOR_BLUE)
                    else:  # Cooperative 2 Player mode
                        self.draw_health_bar(ent, (WIN_WIDTH - 170, WIN_HEIGHT - 60), COLOR_BLUE)
                if ent.name == 'Player2':
                    self.draw_score(ent, (20, 50), COLOR_RED)
                    self.draw_health_bar(ent, (20, WIN_HEIGHT - 60), COLOR_RED)

            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        quit()

                found_player = False
                for ent in self.entity_list:
                    if isinstance(ent, (Player)):
                        found_player = True

                if found_player == False:
                    return False

            # Check if all enemies are destroyed
            if self.count_enemies() == 0:
                # Save score before moving to next level
                for ent in self.entity_list:
                    if isinstance(ent, Player):
                        player_score[0] = ent.score  # Both players share the same score
                        break  # Only need to save once since scores are shared
                return True  # Level cleared

            # Draw level name with larger font and better position
            self.level_text(24, f"{self.name}", COLOR_WHITE, (WIN_WIDTH//2 - 50, 10))
            pygame.display.flip()

            EntityMediator.verify_collision(entity_list=self.entity_list)
            EntityMediator.verify_health(entity_list=self.entity_list)

    def create_enemy_formation(self):
        # Create a grid of enemies
        rows = 3
        cols = 5
        spacing_x = 100  # Increased horizontal spacing
        spacing_y = 70   # Increased vertical spacing
        start_x = (WIN_WIDTH - (cols - 1) * spacing_x) // 2
        start_y = 50     # Start higher on the screen
        
        for row in range(rows):
            for col in range(cols):
                x = start_x + col * spacing_x
                y = start_y + row * spacing_y
                choice = random.choice(('Enemy1', 'Enemy2'))
                enemy = EntityFactory.get_entity(choice)
                enemy.rect.centerx = x
                enemy.rect.centery = y
                enemy.initial_y = y
                self.entity_list.append(enemy)

    def level_text(self, text_size: int, text: str, text_color: tuple[int, int, int], text_pos: tuple[int, int]):
        # Use a more modern font
        text_font: Font = pygame.font.SysFont('Segoe UI', size=text_size, bold=True)
        
        # Create shadow effect
        shadow_color = (0, 0, 0)  # Black shadow
        shadow_offset = 2
        
        # Format level text to add space between "Level" and number
        if text.startswith('Level'):
            text = f"Level {text[5:]}"
        
        # Render shadow
        shadow_surf: Surface = text_font.render(text, True, shadow_color).convert_alpha()
        shadow_rect: Rect = shadow_surf.get_rect(left=text_pos[0] + shadow_offset, top=text_pos[1] + shadow_offset)
        self.window.blit(shadow_surf, shadow_rect)
        
        # Render main text
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(text_surf, text_rect)

    def draw_health_bar(self, player: Player, position: tuple[int, int], color: tuple[int, int, int]):
        # Health bar dimensions
        bar_width = 150  # Increased width
        bar_height = 15  # Increased height
        border_width = 2
        
        # Draw border
        border_rect = pygame.Rect(position[0], position[1], bar_width, bar_height)
        pygame.draw.rect(self.window, COLOR_WHITE, border_rect, border_width)
        
        # Calculate health bar width based on current health
        health_width = int((player.health / 5) * (bar_width - border_width * 2))
        
        # Draw health bar
        health_rect = pygame.Rect(
            position[0] + border_width,
            position[1] + border_width,
            health_width,
            bar_height - border_width * 2
        )
        pygame.draw.rect(self.window, color, health_rect)
        
        # Draw player name with shadow
        text = f'Player {player.name[-1]}'
        text_font: Font = pygame.font.SysFont('Segoe UI', size=16, bold=True)
        
        # Render shadow
        shadow_surf: Surface = text_font.render(text, True, (0, 0, 0)).convert_alpha()
        shadow_rect: Rect = shadow_surf.get_rect(left=position[0] + 2, top=position[1] - 22)
        self.window.blit(shadow_surf, shadow_rect)
        
        # Render main text
        text_surf: Surface = text_font.render(text, True, color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=position[0], top=position[1] - 20)
        self.window.blit(text_surf, text_rect)

    def draw_score(self, player: Player, position: tuple[int, int], color: tuple[int, int, int]):
        text = f'Score: {player.score}'
        text_font: Font = pygame.font.SysFont('Segoe UI', size=16, bold=True)
        
        # Render shadow
        shadow_surf: Surface = text_font.render(text, True, (0, 0, 0)).convert_alpha()
        shadow_rect: Rect = shadow_surf.get_rect(left=position[0] + 2, top=position[1] + 2)
        self.window.blit(shadow_surf, shadow_rect)
        
        # Render main text
        text_surf: Surface = text_font.render(text, True, color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=position[0], top=position[1])
        self.window.blit(text_surf, text_rect)
