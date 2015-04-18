import sys
import random



class BaseDeck():

    cards = []

    def __init__(self, cls, deck=None):
        self._cls = cls
        if (deck is None):
            self.cards = cls.genDeck()
        else:
            self.cards = deck
    

    def drawCard(self):
        return random.choice(self.cards)

    def dispatch_deck(self, playerList, number=-1):
        playerCard = []
        playerNum = len(playerList)
        cardNum = len(self.cards)
        if number == -1:
            cardsperplayer = int(cardNum/playerNum)
        else:
            cardsperplayer = number
        random.shuffle(self.cards)
        for i in range(playerNum):
            t = type(self)(type(self), self.cards[0:cardsperplayer])
            playerCard.append(t)
            self -= t
        return playerCard


    def genDeck():
        raise NotImplementedError()

    def giveCard(self):
        try:
            return self.cards.pop()
        except IndexError:
            return None


    def exchangeCard(self, player):
        pass

    def returnTop(self, cls):
        pass


    def __iadd__(self, other):
        self.cards.append(other.cards)

    def __isub__(self, other):
        for i in other.cards:
            try:
                self.cards.remove(i)
            except ValueError:
                continue
        return self

    def __str__(self):
        re = ""
        for i in self.cards:
            re = re + str(i) + "\n"
        return re

    def __len__(self):
        return len(self.cards)

    def __getitem__(self, val):
        return self.cards[val]

class Basecard():

    def __init__(self):
        raise NotImplementedError()





if __name__ == '__main__':
    t = Basecard([1,2,3,4,5,6])
