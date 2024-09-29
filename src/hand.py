from src.card import Card

class Hand:
    def __init__(self, к = None, о = None, б= None, т = None, м = None):
        if к is None: к = 0
        if о is None: о = 0
        if б is None: б = 0
        if т is None: т = 0
        if м is None: м = 0
        self.к = к
        self.о = о
        self.б = б
        self.т = т
        self.м = м

    def __repr__(self):
        return "к" + str(self.к) + "о" + str(self.о) + "б" + str(self.б) + "т" + str(self.т) + "м" + str(self.м)

    def save(self):
        return repr(self)

    @classmethod
    def load(cls, text: str):
        return Hand(
            int(text[text.find("к") + 1]),
            int(text[text.find("о") + 1]),
            int(text[text.find("б") + 1]),
            int(text[text.find("т") + 1]),
            int(text[text.find("м") + 1])
        )

    def add_card(self, card: Card):
        self.к += card.к
        self.о += card.о
        self.б += card.б
        self.т += card.т
        self.м += card.м

    def score(self, other):
        return self.к * other.к + self.о * other.о + self.б * other.б + self.т * other.т + self.м * other.м
