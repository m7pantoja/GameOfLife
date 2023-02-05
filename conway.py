import game_class

def main():    
    game = game_class.Game()    
    
    while True:
        game.logic()
        game.graphics()
        game.settings()


main()








