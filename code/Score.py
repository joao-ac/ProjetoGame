import sys
from datetime import datetime

import pygame
import pygame.transform
from pygame import Surface, Rect, KEYDOWN, K_RETURN, K_BACKSPACE, K_ESCAPE
from pygame.font import Font

from code.Const import COLOR_YELLOW, SCORE_POS, MENU_OPTION, COLOR_WHITE, WIN_WIDTH, WIN_HEIGHT
from code.DBProxy import DBProxy


class Score:
    def __init__(self, window: Surface):
        self.window = window
        # Load and scale the background image
        original_surf = pygame.image.load('./asset/ScoreBg.png').convert_alpha()
        # Scale to fit screen height while maintaining aspect ratio
        scale_factor = WIN_HEIGHT / original_surf.get_height()
        new_width = int(original_surf.get_width() * scale_factor)
        new_height = int(original_surf.get_height() * scale_factor)
        self.surf = pygame.transform.scale(original_surf, (new_width, new_height))
        # Center the background horizontally
        self.rect = self.surf.get_rect(centerx=WIN_WIDTH/2, top=0)

    def save(self, game_mode: str, player_score: list[int]):
        pygame.mixer_music.load('./asset/Score.wav')
        pygame.mixer_music.set_volume(1.0)  # Set to maximum volume
        pygame.mixer_music.play(-1)
        db_proxy = DBProxy('DBScore')
        name = ''
        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.score_text(48, 'GAME CLEAR', COLOR_YELLOW, SCORE_POS['Title'])
            text = 'Enter Player 1 name (4 characters):'
            score = player_score[0]
            if game_mode == MENU_OPTION[0]:  # 1 Player mode
                score = player_score[0]
            elif game_mode == MENU_OPTION[1]:  # 2 Player cooperative mode
                score = player_score[0]  # Both players share the same score
                text = 'Enter Team name (4 characters):'
            self.score_text(20, text, COLOR_WHITE, SCORE_POS['EnterName'])

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == KEYDOWN:
                    if event.key == K_RETURN and len(name) == 4:
                        db_proxy.save({'name': name, 'score': score, 'date': get_formatted_date()})
                        self.show()
                        return
                    elif event.key == K_BACKSPACE:
                        name = name[:-1]
                    else:
                        if len(name) < 4:
                            name += event.unicode
            self.score_text(20, name, COLOR_WHITE, SCORE_POS['Name'])
            pygame.display.flip()

    def show(self):
        pygame.mixer_music.load('./asset/Score.wav')
        pygame.mixer_music.set_volume(1.0)  # Set to maximum volume
        pygame.mixer_music.play(-1)
        self.window.blit(source=self.surf, dest=self.rect)
        self.score_text(48, 'TOP 10 SCORE', COLOR_YELLOW, SCORE_POS['Title'])
        self.score_text(20, 'NAME     SCORE           DATE      ', COLOR_YELLOW, SCORE_POS['Label'])
        db_proxy = DBProxy('DBScore')
        list_score = db_proxy.retrieve_top10()
        db_proxy.close()

        for player_score in list_score:
            id_, name, score, date = player_score
            self.score_text(20, f'{name}     {score:05d}     {date}', COLOR_YELLOW,
                            SCORE_POS[list_score.index(player_score)])
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        return
            pygame.display.flip()

    def score_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
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


def get_formatted_date():
    current_datetime = datetime.now()
    current_time = current_datetime.strftime("%H:%M")
    current_date = current_datetime.strftime("%d/%m/%y")
    return f"{current_time} - {current_date}"
