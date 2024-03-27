from settings import *

class Score:
    
    def __init__(self):
        self.surface = pygame.Surface((sidebar_width, game_height * score_height - padding))
        self.rect = self.surface.get_rect(bottomright = (window_width - padding, window_height - padding))
        self.display_surface = pygame.display.get_surface()

        self.font = pygame.font.Font("/home/raspudil/workspace/github.com/Revan68/Tetris/images/pixel-operator.ttf", 30)

        self.increment_height = self.surface.get_height() / 3

        self.score = 0
        self.level = 1
        self.lines = 0

    def display_text(self, pos, text):
        text_surface = self.font.render(f'{text[0]}: {text[1]}', True, 'white')
        text_rect = text_surface.get_rect(center = pos)
        self.surface.blit(text_surface, text_rect)

    def run(self):
        self.surface.fill(gray)
        for i, text in enumerate([('Score', self.score), ('Level', self.level), ('Lines', self.lines)]):
            x = self.surface.get_width() / 2
            y = self.increment_height / 2 + i * self.increment_height
            self.display_text((x, y), text)

        self.display_surface.blit(self.surface, self.rect)
        pygame.draw.rect(self.display_surface, yellow, self.rect, 2, 2)