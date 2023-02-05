

class Grid:

    def __init__(self, alive_cells = set()):
        self.alive_cells = alive_cells
        self.cells = {ncell for ac in self.alive_cells for ncell in ac.neighbors()} | self.alive_cells

    def add(self, cell):
        self.alive_cells.add(cell)
        for ncell in cell.neighbors():
            self.cells.add(ncell)

    def remove(self,cell):
        if cell in self.alive_cells:                        
            self.alive_cells.remove(cell)

    def update(self):
        def __alive_neighbors(cell):
            alive_neighbors = 0
            for ncell in cell.neighbors():
                if ncell in self.alive_cells:
                    alive_neighbors += 1
            return alive_neighbors

        new_alive_cells = set()
        for cell in self.cells:
            if __alive_neighbors(cell) == 3:
                new_alive_cells.add(cell)
            if ((__alive_neighbors(cell) == 2) and (cell in self.alive_cells)):
                new_alive_cells.add(cell)

        new_grid = Grid(new_alive_cells)

        self.alive_cells = new_grid.alive_cells
        self.cells = new_grid.cells


    def fit_dimension(self, new_dimension):
        reshaped_alive_cells = {cell.reshape(new_dimension) for cell in self.alive_cells}
        new_grid = Grid(reshaped_alive_cells)
        self.alive_cells = new_grid.alive_cells
        self.cells       = new_grid.cells
        