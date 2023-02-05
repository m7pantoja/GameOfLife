import pygame
import sys
import _grids_class 
import _cell_class


WHITE = (255,255,255)
VERDE_NOCHE = (0,20,20)
SIZE = (1200,750)


class Game:

    clock = pygame.time.Clock()
    screen = pygame.display.set_mode(SIZE)
    start_stop_button = pygame.Rect(500,655,200,60)


    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Game of Life")
        self.grid = _grids_class.Grid()
        self.mode = "Pause"
        self.speed = 20
        self.cell_dim = 10


    def logic(self):

        def __locate_cell(position):
            return _cell_class.Cell(((position[0] // self.cell_dim) * self.cell_dim, 
                                     (position[1] // self.cell_dim) * self.cell_dim),
                                     self.cell_dim)
        
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
                            self.grid.add(__locate_cell(p))
                    if event.button == 3:
                        self.grid.remove(__locate_cell(event.pos))

        if self.mode == "Running":
            self.grid.update()
            for event in pygame.event.get():
                print(event)
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN \
                and event.button == 1 \
                and self.start_stop_button.collidepoint(event.pos):
                    self.mode = "Pause"


    def graphics(self):
        self.screen.fill(VERDE_NOCHE)
        pygame.draw.rect(self.screen, WHITE, self.start_stop_button)

        for x in range(self.cell_dim, SIZE[0], self.cell_dim):
            pygame.draw.line(self.screen, WHITE, [x,0], [x,SIZE[1]])
        for y in range(self.cell_dim, SIZE[1], self.cell_dim):
            pygame.draw.line(self.screen, WHITE, [0,y], [SIZE[0],y])

        for cell in self.grid.alive_cells:
            pygame.draw.rect(self.screen, WHITE, [cell.x, cell.y, cell.dim, cell.dim])


    def settings(self):
        pygame.display.flip()
        self.clock.tick(self.speed)
    
