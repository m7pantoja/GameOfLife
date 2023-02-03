import pygame
from _auxiliar import *



class Grid:

    def __init__(self,alive_cells = []):
        self.alive_cells = noreps(alive_cells)
        self.cells = noreps([ncell for ac in self.alive_cells for ncell in Grid.neighbors(ac)] + self.alive_cells)

    def neighbors(c):
        xs = [pygame.Rect(x, y, CELL_DIM, CELL_DIM)
            for x in range(c.left - CELL_DIM, c.right+ CELL_DIM, CELL_DIM) 
            for y in range(c.top - CELL_DIM, c.bottom + CELL_DIM, CELL_DIM)]
        xs.remove(c)
        return xs

    def add(self, cell):
        if cell in self.alive_cells:
            pass
        else:
            self.alive_cells.append(cell)
            for ncell in Grid.neighbors(cell):
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
            for ncell in Grid.neighbors(c):
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