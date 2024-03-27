from settings import *
from pygame.image import load
from os import path

class Preview:
    
    def __init__(self):
        self.surface = pygame.Surface((sidebar_width, game_height * preview_height))
        self.rect = self.surface.get_rect(topright = (window_width - padding, padding))
        self.display_surface = pygame.display.get_surface()
        
        self.shape_surfaces = {shape: load(f'/home/raspudil/workspace/github.com/Revan68/Tetris/images/{shape}.png').convert_alpha() for shape in tetrominos.keys()}

        self.fragment_height = self.surface.get_height() / 3

    def display_pieces(self, shapes):
        for i, shape in enumerate(shapes):
            shape_surface = self.shape_surfaces[shape]
            x = self.surface.get_width() / 2
            y = self.fragment_height / 2 + i * self.fragment_height
            rect = shape_surface.get_rect(center = (x, y))
            self.surface.blit(shape_surface, rect)

    def run(self, next_shapes):
        self.surface.fill(gray)
        self.display_pieces(next_shapes)
        self.display_surface.blit(self.surface, self.rect)
        pygame.draw.rect(self.display_surface, yellow, self.rect, 2, 2)