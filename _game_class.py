import pygame
import sys
import _grids_class
from _auxiliar import *


class Game():
    
    screen = pygame.display.set_mode(SIZE)
    start_stop_button = pygame.Rect(500,655,200,60)
    clock = pygame.time.Clock()


    def __init__(self):
        self.grid = _grids_class.Grid()
        self.mode = "Pause"
        self.speed = 20 


    def deep_flow(self):
        if self.mode == "Pause":
            for event in pygame.event.get():
                print(event)
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        p = event.pos
                        if self.start_stop_button.collidepoint(p):
                            self.mode = "Running"
                        else:
                            self.grid.add(pygame.Rect((p[0] // CELL_DIM) * CELL_DIM, (p[1] // CELL_DIM) * CELL_DIM, CELL_DIM, CELL_DIM))
                    if event.button == 3:
                        p = event.pos
                        self.grid.remove(pygame.Rect((p[0] // CELL_DIM) * CELL_DIM, (p[1] // CELL_DIM) * CELL_DIM, CELL_DIM, CELL_DIM))
        if self.mode == "Running":
            self.grid.update()
            for event in pygame.event.get():
                print(event)
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN \
                and event.button == 1 \
                and self.start_stop_button.collidepoint(event.pos):
                    self.mode = "Pause"


    def graphics(self):
        self.screen.fill(VERDE_NOCHE)
        pygame.draw.rect(self.screen, WHITE, self.start_stop_button)

        for x in range(CELL_DIM, SIZE[0], CELL_DIM):
            pygame.draw.line(self.screen, WHITE, [x,0], [x,SIZE[1]])
        for y in range(CELL_DIM, SIZE[1], CELL_DIM):
            pygame.draw.line(self.screen, WHITE, [0,y], [SIZE[0],y])

        for cell in self.grid.alive_cells:
            pygame.draw.rect(self.screen, WHITE, cell)
    
    