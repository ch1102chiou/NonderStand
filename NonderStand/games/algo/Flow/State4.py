from NonderStand.lib.BaseState import BaseState



class State4(BaseState):

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
        from NonderStand.games.algo.Flow.State1 import State1 as State1
        if hasattr(self, 'CurrentPlayer') is False:
            self.__class__ =  State1
            return True
        if self.numberOfLivePlayer == 1:
            for  i in self.playerList:
                if self.playerdict[i].isLoss is False:
                    print ("%s is winner!!!" %(i))
                    return False
            print ("Should not enter this section bug found\n")

        if self.CurrentPlayer.isLoss is False:
            print ("It's %s round\n" %(self.CurrentPlayer.name))
            act = self.CurrentPlayer.action(True, self, card)
            while act.updateBoard():
                act = self.CurrentPlayer.action(False, self, card)
        self.__class__ =  State1
        return True
