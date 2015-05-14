import sys
from NonderStand.lib.BaseCard import BaseDeck as BaseDeck
from NonderStand.lib.BaseGame import BaseGame as BaseGame
from AlgoCard import AlgoCard
from AlgoPlayer import AlgoPlayer
from Flow.State1 import State1
#from NonderStand.games.algo.Flow.State1

"""
    Required Property for the MainGame
    1. Name
    2. playersRange
"""

class MainGame(BaseGame):

    Name = "Algo"
    playersRange = range(2,5)

    def __init__(self):
        pass

    def setup(self):
        self.deck = BaseDeck(AlgoCard)
        if len(self.playerlist) == 4:
            dispatch = self.deck.dispatch_deck(self.playerlist, number = 3)
        else:
            dispatch = self.deck.dispatch_deck(self.playerlist, number = 4)
            
        tmp = list(zip(self.playerlist, dispatch))
        for i, j in tmp:
            p = AlgoPlayer(i)
            j.cards.sort()
            p.setCards(j)
            self.player[p.name] = p
            print ("%s cards \n%s" %(p.name, j))
        self._state = State1(self.player, len(self.player))

    def start(self):
        while self._state.getNext(self.deck.giveCard()):
            continue
        
    

if __name__ == '__main__':
    a = MainGame()
    print(a.Name)