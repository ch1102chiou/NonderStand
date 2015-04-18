from NonderStand.lib.BaseCard import Basecard

class PokerLike(Basecard):
    """
    __init__: function to generate PokerLike Instance
    @para colorList: color list, for example A poker have four color
    and each color have 13 cards, it should be 
    [range(1,14), range(1,14), range(1,14), range(1,14)]. 
    If you want to add jokers (two jokers) it should be 
    [range(1,14), range(1,14), range(1,14), range(1,14), range(1,3]
    @ para colorName list, give name of color. For poker, it should be
    ["spade", "heart", "diamond", "club"]
    return value: A PokerLike instance.
    """

    colorList = {}

    def __init__(self, color, value):
        self.color = color
        self.value = value

    @classmethod
    def genDeck(cls):
        tmp = []
        tmpList = zip(list(cls.colorList.keys()), list(cls.colorList.values()))
        tmpList = list(tmpList)
        cardnum = len(tmpList)
        for i, j in tmpList:
            for c in j:
                tmp.append(cls(i, c))
        return tmp

    def __str__(self):
        return "%s %s" %(self.color, self.value)



