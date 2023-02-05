import _game_class


def main():    
    game = _game_class.Game()    
    
    while True:
        game.logic()
        game.graphics()
        game.settings()


main()








