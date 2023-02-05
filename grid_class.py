import numpy as np


class Grid:
    SHAPE = (300,200)

    def __init__(self,alive_cells = set ()):
        self.array = np.zeros((self.SHAPE))
        for cell in alive_cells:
            self.array[cell[0]][cell[1]] = 1

    def add(self, cell):
        self.array[cell[0]][cell[1]] = 1

    def remove(self, cell):
        self.array[cell[0]][cell[1]] = 0

    def __alive_neighbors(array,position):
        return sum(array[x][y] 
            for x in range(position[0]-1, position[0] +2) 
            for y in range(position[1] -1, position[1] + 2) if (x,y) != position)

    def update(self):
        new_alive_cells = set()
        for x in range(self.array.shape[0]-1):
            for y in range(self.array.shape[1]-1):
                if Grid.__alive_neighbors(self.array,(x,y)) == 3:
                    new_alive_cells.add((x,y))
                if ((Grid.__alive_neighbors(self.array,(x,y)) == 2) and (self.array[x][y] == 1)):
                    new_alive_cells.add((x,y))

        new_grid = Grid(new_alive_cells)
        self.array = new_grid.array

    def alive_cells(self):
        alive_cells = set()
        for x in range(self.array.shape[0]):
            for y in range(self.array.shape[1]):
                if self.array[x][y] == 1:
                    alive_cells.add((x,y))
        return alive_cells

    def cell_dim(zoom_level):
        return 800 / (200-(zoom_level)*2)

    def pixel_to_coord(position, zoom_level):
        cell_dim = Grid.cell_dim(zoom_level)
        return (int(position[1] // cell_dim), int(position[0] // cell_dim))
    
    def coord_to_pixel(coord, zoom_level):
        cell_dim = Grid.cell_dim(zoom_level)
        return [cell_dim*coord[1], cell_dim*coord[0] , cell_dim, cell_dim]

