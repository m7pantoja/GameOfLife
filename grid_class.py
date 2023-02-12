import numpy as np


class Grid:
    SHAPE = (300,200)

    def __init__(self,alive_cells = set ()):
        self.array = np.zeros((self.SHAPE))
        for cell in alive_cells:
            self.add(cell)

    def __is_close(cell, shape):
        top_border = cell[1] < 2
        left_border = cell[0] < 2
        bottom_border = cell[1] > shape[1] -2
        right_border = cell[0] > shape[0] -2
        return (top_border, left_border, bottom_border, right_border)

    def __increase_borders(self, borders):
        if borders[0]:
            self.array = np.insert(self.array, 0, np.zeros(self.array.shape[1]), 0)
        if borders[1]:
            self.array = np.insert(self.array, 0, np.zeros(self.array.shape[0]), 1)
        if borders[2]:
            self.array = np.insert(self.array, self.array.shape[0], np.zeros(self.array.shape[1]), 0)
        if borders[3]:
            self.array = np.insert(self.array, self.array.shape[1], np.zeros(self.array.shape[0]), 1)

    def add(self, cell):
        close_borders = Grid.__is_close(cell, self.array.shape)
        self.__increase_borders(close_borders)
        self.array[cell[0]][cell[1]] = 1

    def remove(self, cell):
        self.array[cell[0]][cell[1]] = 0

    def __neighbors(position):
        return {(x,y) for x in range(position[0]-1, position[0] +2) 
            for y in range(position[1] -1, position[1] + 2) if (x,y) != position}    

    def __alive_neighbors(array,position):
        return sum(array[x][y] for (x,y) in Grid.__neighbors(position))

    def alive_cells(self):
        alive_cells = set()
        for x in range(self.array.shape[0]):
            for y in range(self.array.shape[1]):
                if self.array[x][y] == 1:
                    alive_cells.add((x,y))
        return alive_cells

    def activated_cells(self):
        return {ncell for cell in self.alive_cells() for ncell in Grid.__neighbors(cell)}

    def update(self):
        new_alive_cells = set()
        for cell in self.activated_cells():
                if Grid.__alive_neighbors(self.array,cell) == 3:
                    new_alive_cells.add(cell)
                if ((Grid.__alive_neighbors(self.array,cell) == 2) and (self.array[cell[0]][cell[1]] == 1)):
                    new_alive_cells.add(cell)

        self.array.fill(0)
        for cell in new_alive_cells:
            self.add(cell)

    def cell_dim(zoom_level):
        dim_values = [1, 2, 4, 5, 8, 10, 16, 20, 25, 40, 50, 80, 100, 200, 400]
        cell_dict = dict(zip(range(15), dim_values))
        return cell_dict[zoom_level]

    def pixel_to_coord(position, zoom_level):
        cell_dim = Grid.cell_dim(zoom_level)
        return (int(position[1] // cell_dim), int(position[0] // cell_dim))
    
    def coord_to_pixel(coord, zoom_level):
        cell_dim = Grid.cell_dim(zoom_level)
        return [cell_dim*coord[1], cell_dim*coord[0] , cell_dim, cell_dim]

