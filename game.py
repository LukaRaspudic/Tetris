from pygame.sprite import Group
from settings import *
from random import choice
from timer import Timer

class Game:
    
    def __init__(self):
        self.surface = pygame.Surface((game_width, game_height))
        self.display_surface = pygame.display.get_surface()
        self.rect = self.surface.get_rect(topleft = (padding, padding))
        self.sprites = pygame.sprite.Group()

        self.field_data = [[0 for x in range(collumns)] for y in range(rows)]
        self.tetromino = Tetromino(
            choice(list(tetrominos.keys())), 
            self.sprites, 
            self.create_new_tetromino,
            self.field_data
            )

        self.timers = {
            'vertical move': Timer(update_start_speed, True, self.move_down),
            'horizontal move': Timer(move_wait_time)
        }
        self.timers['vertical move'].activate()

    def timer_update(self):
        for timer in self.timers.values():
            timer.update()

    def move_down(self):
        self.tetromino.move_down()

    def draw_grid(self):
        for colm in range(1, collumns):
            x = colm * cell_size
            pygame.draw.line(self.surface, line_colour, (x, 0), (x, self.surface.get_height()), 1)

        for row in range(1, rows):
            y = row * cell_size
            pygame.draw.line(self.surface, line_colour, (0, y), (self.surface.get_height(), y), 1)

    def input(self):
        keys = pygame.key.get_pressed()
        
        if not self.timers['horizontal move'].active:
            if keys[pygame.K_LEFT]:
                self.tetromino.move_horizontal(-1)
                self.timers['horizontal move'].activate()
            if keys[pygame.K_RIGHT]:
                self.tetromino.move_horizontal(1)
                self.timers['horizontal move'].activate()
    
    def create_new_tetromino(self):
        self.tetromino = Tetromino(
            choice(list(tetrominos.keys())), 
            self.sprites, 
            self.create_new_tetromino,
            self.field_data
            )

    def run(self):
        self.input()
        self.timer_update()
        self.sprites.update()
        self.surface.fill(gray)
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
        self.rect = self.image.get_rect(topleft = self.pos * cell_size)
    
    def update(self):
        self.rect.topleft = self.pos * cell_size

    def horizontal_collide(self, x, field_data):
        if not 0 <= x < collumns:
            return True
        if field_data[int(self.pos.y)][x]:
            return True
    
    def vertical_collide(self, y, field_data):
        if y >= rows:
            return True
        if y >= 0 and field_data[y][int(self.pos.x)]:
            return True

class Tetromino:

    def __init__(self, shape, group, create_new_tetromino, field_data):
        self.block_positions = tetrominos[shape]['shape']
        self.colour = tetrominos[shape]['colour']
        self.create_new_tetromino = create_new_tetromino
        self.field_data = field_data

        self.blocks = [Block(group, pos, self.colour) for pos in self.block_positions]
    
    def move_down(self):
        if not self.next_move_vertical_collide(self.blocks, 1):
            for block in self.blocks:
                block.pos.y += 1
        else:
            for block in self.blocks:
                self.field_data[int(block.pos.y)][int(block.pos.x)] = block
            self.create_new_tetromino()
    
    def move_horizontal(self, amount):
        if not self.next_move_horizontal_collide(self.blocks, amount):
            for block in self.blocks:
                block.pos.x += amount

    def next_move_horizontal_collide(self, blocks, amount):
        collision_list = [block.horizontal_collide(int(block.pos.x + amount), self.field_data) for block in self.blocks]
        return True if any(collision_list) else False
    
    def next_move_vertical_collide(self, blocks, amount):
        collision_list = [block.vertical_collide(int(block.pos.y + amount), self.field_data) for block in self.blocks]
        return True if any(collision_list) else False