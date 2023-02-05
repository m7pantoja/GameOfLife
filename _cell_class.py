

class Cell:

    def __init__(self, position, dimension):
        self.pos = position
        self.x   = self.pos[0]
        self.y   = self.pos[1]
        self.dim = dimension

    def __eq__(self, another) -> bool:
        return (self.pos == another.pos) and (self.dim == another.dim)

    def __hash__(self) -> int:
        return hash(((self.pos), self.dim))
    
    def __repr__(self) -> str:
        return "({},{}) : [{}]".format(self.x, self.y, self.dim)

    def neighbors(self):
        return  {Cell((x, y), self.dim)
                for x in range(self.x - self.dim, self.x + 2*self.dim, self.dim) 
                for y in range(self.y - self.dim, self.y + 2*self.dim, self.dim) if (x,y) != self.pos}
    
    def reshape(self, new_dimension):
        return locate_cell(self.pos, new_dimension)


def locate_cell(position, dimension):
    return Cell(((position[0] // dimension) * dimension, 
                 (position[1] // dimension) * dimension),
                 dimension)


