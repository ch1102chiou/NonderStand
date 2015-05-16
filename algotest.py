import sys
from NonderStand.games.algo.AlgoPlayer import AlgoPlayer as AlgoPlayer
from NonderStand.games.algo.AlgoPlayer import AlgoPlayer as AlgoPlayer
from NonderStand.games.algo.AlgoCard import AlgoCard as AlgoCard
from NonderStand.lib.BaseCard import BaseDeck as BaseDeck
from NonderStand.games.algo.Flow.State1 import State1

if __name__ == '__main__':
    sys.path.append("./NonderStand/games/algo")
    from MainGame import MainGame as MainGame
    game = MainGame()
    ## Setup game manually and test it
    game.playerlist = ["a", "b", "c", "d"]
    a = AlgoPlayer("a")
    b = AlgoPlayer("b")
    c = AlgoPlayer("c")
    ##


    ## Setup the cards
    
    t1 = AlgoCard("white", 1)
    t2 = AlgoCard("white", 3)
    t3 = AlgoCard("black", 4)
    da = BaseDeck(AlgoCard, [t1, t2, t3])
    a.setCards(da)

    t1 = AlgoCard("black", 1)
    t2 = AlgoCard("white", 4)
    t3 = AlgoCard("black", 5)
    db = BaseDeck(AlgoCard, [t1, t2, t3])
    b.setCards(db)

    t1 = AlgoCard("black", 2)
    t2 = AlgoCard("white", 2)
    t3 = AlgoCard("white", 6)
    dc = BaseDeck(AlgoCard, [t1, t2, t3])
    c.setCards(dc)

    
    t1 = AlgoCard("black", 3)
    t2 = AlgoCard("black", 6)
    t3 = AlgoCard("white", 5)

    dg = BaseDeck(AlgoCard, [t1, t2, t3])
    game.deck = dg

    ## Setup Player to game
    game.player["a"] = a
    game.player["b"] = b
    game.player["c"] = c
    ##



    game._state = State1(game.player, len(game.player))
    game.start()






