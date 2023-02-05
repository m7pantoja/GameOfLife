

class Cell:

    def __init__(self, position, dimension):
        self.pos = position
        self.x   = self.pos[0]
        self.y   = self.pos[1]
        self.dim = dimension

    def __eq__(self, __o: object, /) -> bool:
        return (self.pos == __o.pos) and (self.dim == __o.dim)

    def __hash__(self) -> int:
        return id(self)
    
    def __repr__(self) -> str:
        return "({},{}) : [{}]".format(self.x, self.y, self.dim)

    def neighbors(self):
        return  list({Cell((x, y), self.dim)
                for x in range(self.x - self.dim, self.x + 2*self.dim, self.dim) 
                for y in range(self.y - self.dim, self.y + 2*self.dim, self.dim) if (x,y) != self.pos})