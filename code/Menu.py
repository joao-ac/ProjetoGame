#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
import pygame.transform
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import WIN_WIDTH, WIN_HEIGHT, COLOR_ORANGE, MENU_OPTION, COLOR_WHITE, COLOR_YELLOW


class Menu:
    def __init__(self, window):
        self.window = window
        # Load and scale the background image
        original_surf = pygame.image.load("./asset/MenuBg.png").convert_alpha()
        # Scale to fit screen height while maintaining aspect ratio
        scale_factor = WIN_HEIGHT / original_surf.get_height()
        new_width = int(original_surf.get_width() * scale_factor)
        new_height = int(original_surf.get_height() * scale_factor)
        self.surf = pygame.transform.scale(original_surf, (new_width, new_height))
        # Center the background horizontally
        self.rect = self.surf.get_rect(centerx=WIN_WIDTH/2, top=0)

    def run(self, ):
        menu_option = 0
        pygame.mixer_music.load("./asset/Menu.mp3")
        pygame.mixer_music.play(-1)
        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(text_size=50, text="Space", text_color=COLOR_ORANGE, text_center_pos=((WIN_WIDTH / 2), 70))
            self.menu_text(text_size=50, text="Invader", text_color=COLOR_ORANGE, text_center_pos=((WIN_WIDTH / 2), 110))

            for i in range(len(MENU_OPTION)):
                if i == menu_option:
                    self.menu_text(text_size=20, text=MENU_OPTION[i], text_color=COLOR_YELLOW, text_center_pos=((WIN_WIDTH / 2), 170 + 20 * i))
                else:
                    self.menu_text(text_size=20, text=MENU_OPTION[i], text_color=COLOR_WHITE, text_center_pos=((WIN_WIDTH / 2), 170 + 20 * i))

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        if menu_option < len(MENU_OPTION) - 1:
                            menu_option += 1
                        else: menu_option = 0

                    if event.key == pygame.K_UP:
                        if menu_option > 0:
                            menu_option -= 1
                        else: menu_option = len(MENU_OPTION) - 1

                    if event.key == pygame.K_RETURN:
                        return MENU_OPTION[menu_option]

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont("Lucida Sans Typewriter", text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(text_surf, text_rect)