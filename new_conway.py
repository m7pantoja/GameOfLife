import pygame
import _game_class


def main():
    pygame.init()
    pygame.display.set_caption("Game of Life")
    game = _game_class.Game()    

    while True:
        game.deep_flow()
        game.graphics()

        pygame.display.flip()
        game.clock.tick(game.speed)



main()