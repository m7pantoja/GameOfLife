import pygame
import grid_class

WHITE = (255,255,255)
BLUE = (176,224,230)
VERDE_NOCHE = (0,20,20)
SIZE = (1200,800)

class Game:
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode(SIZE)
    graphic_blocks = []
    start_stop_button = pygame.Rect(505,655,200,60)
    graphic_blocks.append(start_stop_button)

    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Game of Life")
        self.grid = grid_class.Grid()
        self.mode = "Pause"
        self.speed = 20
        self.zoom_level = 5

    def logic(self):
        if self.mode == "Pause":
            for event in pygame.event.get():
                print(event)
                if event.type == pygame.QUIT:
                    quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        p = event.pos
                        if self.start_stop_button.collidepoint(p):
                            self.mode = "Running"
                        else:
                            self.grid.add(grid_class.Grid.pixel_to_coord(p, self.zoom_level))
                            self.mode = "Selection"
                    if event.button == 3:
                        self.grid.remove(grid_class.Grid.pixel_to_coord(event.pos, self.zoom_level))
                if event.type == pygame.MOUSEWHEEL:
                    if (event.y < 0) and (event.y + self.zoom_level > 1):
                        self.zoom_level += event.y
                    if (event.y > 0) and (self.zoom_level + event.y < 14):
                        self.zoom_level += event.y
        if self.mode == "Running":
            self.grid.update()
            for event in pygame.event.get():
                print(event)
                if event.type == pygame.QUIT:
                    quit()
                if event.type == pygame.MOUSEBUTTONDOWN \
                and event.button == 1 \
                and self.start_stop_button.collidepoint(event.pos):
                    self.mode = "Pause"
                if event.type == pygame.MOUSEWHEEL:
                    if (event.y < 0) and (event.y + self.zoom_level > 1):
                        self.zoom_level += event.y
                    if (event.y > 0) and (self.zoom_level + event.y < 14):
                        self.zoom_level += event.y
        if self.mode == "Selection":
            for event in pygame.event.get():
                print(event)
                if event.type != pygame.MOUSEBUTTONUP:
                    p = event.pos
                    self.grid.add(grid_class.Grid.pixel_to_coord(p, self.zoom_level))
                else:
                    self.mode = "Pause"
                    
    def graphics(self):
        self.screen.fill(VERDE_NOCHE)
        cell_dim = int(grid_class.Grid.cell_dim(self.zoom_level))

        for x in range(cell_dim, SIZE[0], cell_dim):
            pygame.draw.line(self.screen, WHITE, [x,0], [x,SIZE[1]])
        for y in range(cell_dim, SIZE[1], cell_dim):
            pygame.draw.line(self.screen, WHITE, [0,y], [SIZE[0],y])

        for cell in self.grid.alive_cells():
            pygame.draw.rect(self.screen, WHITE, grid_class.Grid.coord_to_pixel(cell, self.zoom_level))

        for block in self.graphic_blocks:
            pygame.draw.rect(self.screen, BLUE, block)

    def settings(self):
        pygame.display.flip()
        self.clock.tick(self.speed)
    
