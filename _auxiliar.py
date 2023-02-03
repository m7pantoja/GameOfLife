

CELL_DIM = 10                # (Integer)
WHITE = (255,255,255)
VERDE_NOCHE = (0,20,20)
SIZE = (1200,750)


def noreps(xs):
    # takes a list and returns a list with no reps 
    ys = []
    for x in xs:
        if x not in ys:
            ys.append(x)
    return ys

