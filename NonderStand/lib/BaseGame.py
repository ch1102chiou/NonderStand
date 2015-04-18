import sys
import re
class BaseGame(object):

    playerlist = []
    player = {}

    def getReady(self):
        print ("Welcome to join %s!!! Please enter the players" %(self.Name))
        print ("Example: Joe Charles Noner Howard")
        while(True):
            players = sys.stdin.readline()
            players = players.strip("\n")
            playerlist = re.split("\s", players)
            for i in playerlist:
                self.addplayer(i)
            if len(playerlist) in self.playersRange:
                break
            else:
                print ("Players should in %s", self.playersRange)
                self.kickoffAll()



    def addplayer(self, player):
        self.playerlist.append(player)
    
    
    def kickoffAll(self):
        self.playerlist = []