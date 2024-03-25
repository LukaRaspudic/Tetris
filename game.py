from pygame.sprite import Group
from settings import *
from random import choice

class Game:
    
    def __init__(self):
        self.surface = pygame.Surface((game_width, game_height))
        self.display_surface = pygame.display.get_surface()
        self.rect = self.surface.get_rect(topleft = (padding, padding))
        self.sprites = pygame.sprite.Group()

        self.tetromino = Tetromino(choice(list(tetrominos.keys())), self.sprites)

    def draw_grid(self):
        for colm in range(1, collumns):
            x = colm * cell_size
            pygame.draw.line(self.surface, line_colour, (x, 0), (x, self.surface.get_height()), 1)

        for row in range(1, rows):
            y = row * cell_size
            pygame.draw.line(self.surface, line_colour, (0, y), (self.surface.get_height(), y), 1)

    def run(self):
        self.sprites.draw(self.surface)
        self.draw_grid()
        self.display_surface.blit(self.surface, (padding, padding))
        pygame.draw.rect(self.display_surface, yellow, self.rect, 2, 2)

class Block(pygame.sprite.Sprite):
    
    def __init__(self, group, pos, colour):
        super().__init__(group)
        self.image = pygame.Surface((cell_size, cell_size))
        self.image.fill(colour)

        self.pos = pygame.Vector2(pos) + block_offset
        x = self.pos.x * cell_size
        y = self.pos.y * cell_size
        self.rect = self.image.get_rect(topleft = (x, y))

class Tetromino:

    def __init__(self, shape, group):
        self.block_positions = tetrominos[shape]['shape']
        self.colour = tetrominos[shape]['colour']

        self.blocks = [Block(group, pos, self.colour) for pos in self.block_positions]