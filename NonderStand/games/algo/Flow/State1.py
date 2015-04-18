from NonderStand.lib.BaseState import BaseState
from NonderStand.games.algo.Flow.State2 import State2 as State2
from NonderStand.games.algo.Flow.State3 import State3 as State3
from NonderStand.games.algo.Flow.State4 import State4 as State4

class State1(BaseState):

    def __init__(self, playerdict, numberOfLivePlayer):
        self.playerdict = playerdict
        self.playerList = list(playerdict.keys())
        self.CurrentPlayer = self.playerdict[self.playerList[0]]
        self.numberOfLivePlayer = numberOfLivePlayer
        try:
            State1.CurrentPlayer = self.playerdict[self.playerList[0]]
            State1.name          = self.playerList[0]
            print(State1.name)
            State2.CurrentPlayer = self.playerdict[self.playerList[1]]
            State2.name          = self.playerList[1]
            print(State2.name)
            State3.CurrentPlayer = self.playerdict[self.playerList[2]]
            State3.name          = self.playerList[2]
            print(State3.name)
            State4.CurrentPlayer = self.playerdict[self.playerList[3]]
            State4.name          = self.playerList[3]
            print(State4.name)
        except IndexError:
            return



    def getNext(self, card=None):
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
        print(type(self))
        self.__class__ =  State2
        return True


