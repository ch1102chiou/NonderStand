from NonderStand.lib.BaseState import BaseState
from NonderStand.games.algo.Flow.State3 import State3 as State3


class State2(BaseState):

    def __init__(self, playerdict, numberOfLivePlayer):
        self.playerdict = playerdict
        self.playerList = list(playerdict.keys())
        self.CurrentPlayer = self.playerdict[self.playerList[0]]
        self.numberOfLivePlayer = numberOfLivePlayer
        try:
            State1.CurrentPlayer = self.playerdict[self.playerList[0]]
            State1.name          = self.playerList[0]

            State2.CurrentPlayer = self.playerdict[self.playerList[1]]
            State2.name          = self.playerList[1]

            State3.CurrentPlayer = self.playerdict[self.playerList[2]]
            State3.name          = self.playerList[2]

            State4.CurrentPlayer = self.playerdict[self.playerList[3]]
            State4.name          = self.playerList[3]

        except IndexError:
            return



    def getNext(self, card=None):
        print(type(self))
        print ("It's %s round\n" %(self.CurrentPlayer.name))
        if self.numberOfLivePlayer == 1:
            for  i in self.playerList:
                if self.playerdict[i].isLoss is False:
                    print ("%s is winner!!!" %(i))
                    return False
            print ("Should not enter this section bug found\n")

        if self.CurrentPlayer.isLoss is False:
            act = self.CurrentPlayer.action(True, self, card)
            while act.updateBoard():
                act = self.CurrentPlayer.action(False, self, card)
        self.__class__ =  State3
        return True
