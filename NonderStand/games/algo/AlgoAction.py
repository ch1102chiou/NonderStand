import sys
from NonderStand.lib.BaseAction import BaseAction
from NonderStand.IOutil.test import getLine



class AlgoAction(BaseAction):

    def __init__(self, state,card=None):
        self.state = state
        self.currentcard = card
        pass

    def setProcedure(self, firstrun):
        if not firstrun:
            self.continueguess = self._setcontinueguess()
            if self.continueguess is False:
                return
        self.continueguess = True
        if self.currentcard is None: # No card from deck, need to use own card
            self._getplayercard()
        self._setplayer()
        self._setindex()
        self._setguessnumber()

    def _setplayer(self):
        print ("Choice the player\n");
        while True:
            line = getLine()
            line = line.strip("\n")
            if line in set(self.state.playerdict.keys()):
                self.player = line
                break
            else:
                print ("No this player. Please choice again\n")

    def _setindex(self):
        print ("Choice the index\n");
        while True:
            line = getLine()
            line = line.strip("\n")
            self.index = int(line)
            try:
                k = self.state.playerdict[self.player].deck.cards[self.index]
                break
            except IndexError:
                print ("No this card. Please choice again\n")
                continue
        
    def _setguessnumber(self):
        print ("Choice the number\n");
        while True:
            line = getLine()
            line = line.strip("\n")
            guess  = int(line)
            if guess in range(0,12):
                self.guessnumber = guess
                break
            else:
                print("Not in the card range (0 ~ 11) please guess number again\n")
                continue



    def _setcontinueguess(self):

        while True:
            print("Do you want to guess again? y/n")
            line = getLine()
            line = line.strip("\n")
            if line == "y":
                return True
            elif line == "n":
                return False

    def _getplayercard(self):
        while True:
            print ("No cards in the public deck, Which card you want to use?")
            line = getLine()
            line = line.strip("\n")
            index = int(line)
            #break
            try:
                self.currentcard = self.state.CurrentPlayer.deck.cards[index]
                break
            except IndexError:
                print("No card")
                continue


    def updateBoard(self):
        if self.continueguess is False:
            if self.currentcard not in self.state.CurrentPlayer.deck.cards:
                self.state.CurrentPlayer.deck.cards.append(self.currentcard)
                self.state.CurrentPlayer.deck.cards.sort()
                self.state.CurrentPlayer.HP = self.state.CurrentPlayer.HP + 1
            return False
        for i in self.state.playerdict[self.player].deck:
            print (i)
        card = self.state.playerdict[self.player].deck.cards[self.index]
        print ("Answer card %d , guess %d" %(card.value,self.guessnumber))
        if card.value == self.guessnumber:
            print ("Correct\n");
            card.setPublic()
            self.state.playerdict[self.player].HP = self.state.playerdict[self.player].HP - 1
            if self.state.playerdict[self.player].HP == 0:
                self.state.playerdict[self.player].isLose = True
                self.state.numberOfLivePlayer = self.state.numberOfLivePlayer - 1
                print ("Player %s has no card!" %(self.state.playerdict[self.player].name))
            return True
        else:
            print ("Not Correct\n");
            if self.state.CurrentPlayer.HP == 0:
                self.state.CurrentPlayer.isLose = True
                print ("Player %s has no card!!!\n" %(state.name))
            self.currentcard.setPublic()
            if self.currentcard not in self.state.CurrentPlayer.deck.cards:
                self.state.CurrentPlayer.deck.cards.append(self.currentcard)
            self.state.CurrentPlayer.deck.cards.sort()
            return False







