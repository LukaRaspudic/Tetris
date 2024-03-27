from settings import *
from pygame.image import load
from os import path

class Preview:
    
    def __init__(self, next_shapes):
        self.surface = pygame.Surface((sidebar_width, game_height * preview_height))
        self.rect = self.surface.get_rect(topright = (window_width - padding, padding))
        self.display_surface = pygame.display.get_surface()
        
        self.next_shapes = next_shapes
        self.shape_surfaces = {shape: load(path.join('..','images',f'{shape}.png')).convert_alpha() for shape in tetrominos.keys()}

    def run(self):
        self.surface.fill(gray)
        self.display_surface.blit(self.surface, self.rect)
        pygame.draw.rect(self.display_surface, line_colour, self.rect, 2, 2)