import sys 
import os
import re


if __name__ == '__main__':
    ## List the avaiable game to create
    gamelist = os.listdir("./NonderStand/games")
    print ("Here is games installed in this server")
    for i in gamelist:
        if i == "__init__.py":
            continue
        print ("%s" %(i))
    ##
    while(True):
        print ("Select the game you want to play")
        gameselect = sys.stdin.readline()
        gameselect = gameselect.strip("\n")
        if gameselect not in gamelist:
            print ("The game %s is not installed in this server" %(gameselect))
            continue
        print ("Prepare the game %s" %(gameselect))
        break
    ##
    ## Host the game
    sys.path.append("./NonderStand/games/" + gameselect)
    from MainGame import MainGame as MainGame
    game = MainGame()
    game.getReady()
    game.setup()
    game.start()