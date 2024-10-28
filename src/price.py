'''Стоимость овощей'''
from random import choice
from src.const import Const


class Price:
    vegetables = ['к', 'о', 'б', 'т', 'м']

    def __init__(self, к=None, о=None, б=None, т=None, м=None):
        if all(veg is None for veg in [к, о, б, т, м]):
            num = [0, 1, 2, 3, 4]
            for veg in self.vegetables:
                setattr(self, veg, choice(num))
                num.remove(getattr(self, veg))
        else:
            veg = [к, о, б, т, м]
            for i in range(5):
                if veg[i] is None:
                    setattr(self, self.vegetables[i], 0)
                else:
                    setattr(self, self.vegetables[i], veg[i])
        if not all(0 <= getattr(self, veg) <= 5 for veg in self.vegetables):
            raise ValueError

    def __repr__(self):
        return "к" + str(self.к) + "о" + str(self.о) + "б" + str(self.б) + "т" + str(self.т) + "м" + str(self.м)

    def __eq__(self, other):
        return self.к == other.к and self.м == other.м \
            and self.т == other.т and self.б == other.б and self.о == other.о

    def add(self, card: str):
        self.к = (self.к + card.count("к")) % (Const.max_price.value + 1)
        self.о = (self.о + card.count("о")) % (Const.max_price.value + 1)
        self.б = (self.б + card.count("б")) % (Const.max_price.value + 1)
        self.т = (self.т + card.count("т")) % (Const.max_price.value + 1)
        self.м = (self.м + card.count("м")) % (Const.max_price.value + 1)

    def save(self):
        return repr(self)

    @staticmethod
    def load(text: str):
        """From 'к4о2б3т0м1' to Price(4, 2, 3, 0, 1)"""
        return Price(
            int(text[text.find("к") + 1]),
            int(text[text.find("о") + 1]),
            int(text[text.find("б") + 1]),
            int(text[text.find("т") + 1]),
            int(text[text.find("м") + 1])
            )
