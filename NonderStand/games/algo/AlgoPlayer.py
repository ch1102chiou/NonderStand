from NonderStand.lib.BasePlayer import BasePlayer
from NonderStand.games.algo.AlgoAction import AlgoAction as AlgoAction
import sys
import re
class AlgoPlayer(BasePlayer):

    def __init__(self, name):
        self.isLoss = False
        super().__init__(name)



    def action(self, isFirstguess, state ,card):
        act = AlgoAction(state, card)
        act.setProcedure(isFirstguess)
        print ("player %s turn got card %s" %(self.name, card))
        return act


    def setCards(self, cards):
        self.deck = cards
        self.HP = len(cards)

    def __str__(self):
        return str(name)

    def addCard(self, card):
        pass
