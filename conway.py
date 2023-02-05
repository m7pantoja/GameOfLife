import _game_class


def main():    
    game = _game_class.Game()    
    
    while True:
        game.logic()
        game.graphics()
        game.settings()


main()


# El problema está en que los objetos de Cell son unhasheables y los estás intentando meter en un set







