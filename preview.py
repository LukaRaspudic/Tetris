from settings import *

class Preview:
    
    def __init__(self):
        self.surface = pygame.Surface((sidebar_width, game_height * preview_height))
        self.rect = self.surface.get_rect(topright = (window_width - padding, padding))
        self.display_surface = pygame.display.get_surface()

    def run(self):
        self.display_surface.blit(self.surface, self.rect)