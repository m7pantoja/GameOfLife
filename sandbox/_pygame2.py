import pygame
import sys

# Variables y constantes:

VERDE_NOCHE = (0,20,20)
WHITE = (255,255,255)

size = (800,500)

class Cuadrado:
    
    def __init__(self,vs):
        self.v1 = vs[0]
        self.v2 = vs[1]
        self.xmax = max(self.v1[0],self.v2[0])
        self.xmin = min(self.v1[0],self.v2[0])
        self.ymax = max(self.v1[1],self.v2[1])
        self.ymin = min(self.v1[1],self.v2[1])


    def ispointin(self,point):
        return (point[0] >= self.xmin and point[0] <= self.xmax) \
                and (point[1] >= self.ymin and point[1] <= self.ymax)

red = [Cuadrado(((x,y),(x+20,y+20))) for x in range(0,820,20) for y in range(0,520,20)]

def vert_square(v):
    for c in red:
        if c.ispointin(v):
            return c
    else:
        return None

# -----------------------------------------------------------------------------------------

pygame.init()
screen = pygame.display.set_mode(size)
highlighted_squares = []

while True:
    screen.fill(VERDE_NOCHE)

    for y in range(20,520,20):
        pygame.draw.line(screen, WHITE, [0,y], [800,y])

    for x in range(20,820,20):
        pygame.draw.line(screen, WHITE, [x,0], [x,500])
    
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                highlighted_squares.append(vert_square(event.pos))
            if event.button == 3:
                c = vert_square(event.pos)
                try:
                    highlighted_squares.remove(c)
                except ValueError:
                    pass

    for c in highlighted_squares:
        pygame.draw.rect(screen, WHITE, [c.v1[0], c.v1[1], 20, 20])

    pygame.display.flip()
