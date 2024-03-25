from settings import *

class Score:
    
    def __init__(self):
        self.surface = pygame.Surface((sidebar_width, game_height * score_height - padding))
        self.rect = self.surface.get_rect(bottomright = (window_width - padding, window_height - padding))
        self.display_surface = pygame.display.get_surface()

    def run(self):
        self.display_surface.blit(self.surface, self.rect)