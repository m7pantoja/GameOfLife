import pygame
import sys
from functools import reduce

## ---------------------------------------------- VARIABLES, CONSTANTES Y DEFINICIONES PREVIAS
pygame.init()

SIZE = (1200,750)
SCREEN = pygame.display.set_mode(SIZE)
START_STOP_BUTTON = pygame.Rect(500,655,200,60)
CELL_DIM = 10    # (Integer)

# Funciones Auxiliares

def noreps(xs):
    # - takes a list and returns a list with no reps 
    ys = []
    for x in xs:
        if x not in ys:
            ys.append(x)
    return ys

# Red de Células

def _neighbors(c):
    xs = [pygame.Rect(x, y, CELL_DIM, CELL_DIM)
        for x in range(c.left - CELL_DIM, c.right+ CELL_DIM, CELL_DIM) 
        for y in range(c.top - CELL_DIM, c.bottom + CELL_DIM, CELL_DIM)]
    xs.remove(c)
    return xs

class Grid:

    def __init__(self,alive_cells = []):
        self.alive_cells = noreps(alive_cells)
        self.cells = noreps([ncell for ac in self.alive_cells for ncell in _neighbors(ac)] + self.alive_cells)

    def add(self, cell):
        if cell in self.alive_cells:
            pass
        else:
            self.alive_cells.append(cell)
            for ncell in _neighbors(cell):
                if ncell in self.cells:
                    pass
                else:
                    self.cells.append(ncell)

    def remove(self,cell):                             
        if cell not in self.alive_cells:
            pass
        else:
            self.alive_cells.remove(cell)

    def update(self):
        def _alive_neighbors(c):
            alive_neighbors = 0
            for ncell in _neighbors(c):
                if ncell in self.alive_cells:
                    alive_neighbors += 1
            return alive_neighbors

        new_alive_cells = []
        for cell in self.cells:
            if _alive_neighbors(cell) == 3:
                new_alive_cells.append(cell)
            elif ((_alive_neighbors(cell) == 2) and (cell in self.alive_cells)):
                new_alive_cells.append(cell)
            else:
                pass

        new_grid = Grid(new_alive_cells)

        self.alive_cells = new_grid.alive_cells
        self.cells = new_grid.cells

# Colores
     
WHITE = (255,255,255)
VERDE_NOCHE = (0,20,20)


## ------------------------------------------------------------------ JUEGO
mycells = Grid()
done = False

while not done:

    # Funcionamiento interno del Juego

    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                p = event.pos
                if START_STOP_BUTTON.collidepoint(p):
                    done = True
                else:
                    mycells.add(pygame.Rect((p[0] // CELL_DIM) * CELL_DIM, (p[1] // CELL_DIM) * CELL_DIM, CELL_DIM, CELL_DIM))
            elif event.button == 3:
                p = event.pos
                mycells.remove(pygame.Rect((p[0] // CELL_DIM) * CELL_DIM, (p[1] // CELL_DIM) * CELL_DIM, CELL_DIM, CELL_DIM))

    # Objetos Gráficos

    SCREEN.fill(VERDE_NOCHE)
    pygame.draw.rect(SCREEN, WHITE, START_STOP_BUTTON)

    for x in range(CELL_DIM, SIZE[0], CELL_DIM):
        pygame.draw.line(SCREEN, WHITE, [x,0], [x,SIZE[1]])
    for y in range(CELL_DIM, SIZE[1], CELL_DIM):
        pygame.draw.line(SCREEN, WHITE, [0,y], [SIZE[0],y])

    for cell in mycells.alive_cells:
        pygame.draw.rect(SCREEN, WHITE, cell)

    # Ajustes

    pygame.display.flip()
    pygame.time.Clock().tick(20)

else:
    while done:

        # Funcionamiento interno del Juego

        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    p = event.pos
                    if START_STOP_BUTTON.collidepoint(p):
                        done = False
            
        # Objetos Gráficos

        SCREEN.fill(VERDE_NOCHE)
        pygame.draw.rect(SCREEN, WHITE, START_STOP_BUTTON)

        for x in range(CELL_DIM, SIZE[0], CELL_DIM):
            pygame.draw.line(SCREEN, WHITE, [x,0], [x,SIZE[1]])
        for y in range(CELL_DIM, SIZE[1], CELL_DIM):
            pygame.draw.line(SCREEN, WHITE, [0,y], [SIZE[0],y])

        for cell in mycells.alive_cells:
            pygame.draw.rect(SCREEN, WHITE, cell)

        # Ajustes

        mycells.update()
        pygame.display.flip()
        pygame.time.Clock().tick(10)

        