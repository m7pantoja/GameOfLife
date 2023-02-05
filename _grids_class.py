

class Grid:

    def __init__(self, alive_cells = []):
        self.alive_cells = alive_cells
        self.cells = list({ncell for ac in self.alive_cells for ncell in ac.neighbors()} | set(self.alive_cells))

    def add(self, cell):
        self.alive_cells.append(cell)
        for ncell in cell.neighbors():
            self.cells.append(ncell)

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

        new_alive_cells = []
        for cell in self.cells:
            if __alive_neighbors(cell) == 3:
                new_alive_cells.append(cell)
            if ((__alive_neighbors(cell) == 2) and (cell in self.alive_cells)):
                new_alive_cells.append(cell)

        new_grid = Grid(new_alive_cells)

        self.alive_cells = new_grid.alive_cells
        self.cells = new_grid.cells