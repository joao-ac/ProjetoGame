#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
import pygame.transform
import os
from pygame import Surface, Rect, KEYDOWN, K_UP, K_DOWN, K_RETURN, K_ESCAPE
from pygame.font import Font

from code.Const import WIN_WIDTH, WIN_HEIGHT, COLOR_ORANGE, MENU_OPTION, COLOR_WHITE, COLOR_YELLOW, ENTITY_SPEED
from code.Background import Background


class Menu:
    def __init__(self, window: Surface):
        self.window = window
        self.menu_text_size = 48
        self.option_text_size = 32
        self.selected = 0
        self.background_list = []
        
        # Load all menu background images
        i = 0
        while True:
            bg_name = f'MenuBg{i}'
            if bg_name not in ENTITY_SPEED:
                break
                
            try:
                # Create four copies of each background for seamless looping
                # Top row
                bg1 = Background(bg_name, (0, 0))
                bg2 = Background(bg_name, (WIN_WIDTH, 0))
                # Bottom row
                bg3 = Background(bg_name, (0, WIN_HEIGHT))
                bg4 = Background(bg_name, (WIN_WIDTH, WIN_HEIGHT))
                
                self.background_list.extend([bg1, bg2, bg3, bg4])
                i += 1
            except Exception as e:
                print(f"Error loading background {bg_name}: {e}")
                break

        # If no backgrounds were loaded, create a default black background
        if not self.background_list:
            print("No menu backgrounds found, using default black background")
            self.background_list = [Background('MenuBg0', (0, 0))]  # Use first menu background as fallback

    def run(self):
        pygame.mixer_music.load("./asset/Menu.wav")
        pygame.mixer_music.set_volume(1.0)  # Set to maximum volume
        pygame.mixer_music.play(-1)  # -1 means loop indefinitely
        while True:
            self.window.fill((0, 0, 0))
            
            # Update and draw backgrounds
            for bg in self.background_list:
                bg.move()
                self.window.blit(source=bg.surf, dest=bg.rect)
            
            self.menu_text(self.menu_text_size, 'Galactic Odyssey', COLOR_YELLOW, (WIN_WIDTH/2, WIN_HEIGHT/4))
            
            for i in range(len(MENU_OPTION)):
                color = COLOR_YELLOW if i == self.selected else COLOR_WHITE
                self.menu_text(self.option_text_size, MENU_OPTION[i], color, 
                             (WIN_WIDTH/2, WIN_HEIGHT/2 + i * 50))

            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_UP:
                        self.selected = (self.selected - 1) % len(MENU_OPTION)
                    elif event.key == K_DOWN:
                        self.selected = (self.selected + 1) % len(MENU_OPTION)
                    elif event.key == K_RETURN:
                        return MENU_OPTION[self.selected]
                    elif event.key == K_ESCAPE:
                        pygame.quit()
                        quit()

            pygame.display.flip()

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        # Special handling for the title
        if text == 'Galactic Odyssey':
            # Create a larger, bolder font for the title
            text_font: Font = pygame.font.SysFont(name="Impact", size=text_size + 20)
            
            # Create outline effect
            outline_color = (0, 0, 0)  # Black outline
            outline_size = 3
            
            # Render the outline
            for offset_x in range(-outline_size, outline_size + 1):
                for offset_y in range(-outline_size, outline_size + 1):
                    outline_surf = text_font.render(text, True, outline_color).convert_alpha()
                    outline_rect = outline_surf.get_rect(center=(text_center_pos[0] + offset_x, text_center_pos[1] + offset_y))
                    self.window.blit(source=outline_surf, dest=outline_rect)
            
            # Render the main text
            text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
            text_rect: Rect = text_surf.get_rect(center=text_center_pos)
            self.window.blit(source=text_surf, dest=text_rect)
        else:
            # Regular text for menu options with shadow
            text_font: Font = pygame.font.SysFont(name="Segoe UI", size=text_size, bold=True)
            
            # Create shadow effect
            shadow_color = (0, 0, 0)  # Black shadow
            shadow_offset = 2
            
            # Render shadow
            shadow_surf: Surface = text_font.render(text, True, shadow_color).convert_alpha()
            shadow_rect: Rect = shadow_surf.get_rect(center=(text_center_pos[0] + shadow_offset, text_center_pos[1] + shadow_offset))
            self.window.blit(source=shadow_surf, dest=shadow_rect)
            
            # Render main text
            text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
            text_rect: Rect = text_surf.get_rect(center=text_center_pos)
            self.window.blit(source=text_surf, dest=text_rect)