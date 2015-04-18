
from NonderStand.lib.Poker import PokerLike

class AlgoCard(PokerLike):


    colorList = {"black": range(0,12),
                 "white": range(0,12)}

    def __init__(self, color, value):
        self.isPublic = False
        super().__init__(color, value)


    def __cmp__(self, other):
        if self.value != other.value:
            return self.value - other.value
        elif self.color == "white":
            return 1
        else:
            return 0


    def setPublic(self):
        self.isPublic = True

    def __str__(self):
        return "%s %s" %(self.color, self.value)

    def __lt__(self, other):
        return self.value < other.value or (self.value == other.value and other.value == "white")

    def __eq__(self, other):
        return self.value == other.value and self.color == other.color

