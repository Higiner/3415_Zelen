'''Стоимость овощей'''

class Price:

    def __init__(self, к = None, о = None, б= None, т = None, м = None):
        if к is None: к = 0
        if о is None: о = 0
        if б is None: б = 0
        if т is None: т = 0
        if м is None: м = 0
        if 0 <= к <= 5 and 0 <= о <= 5 and 0 <= б <= 5 and 0 <= т <= 5 and 0 <= м <= 5 :
            self.к = к
            self.о = о
            self.б = б
            self.т = т
            self.м = м
        else:
            raise ValueError

    def __repr__(self):
        return "к" + str(self.к) + "о" + str(self.о) + "б" + str(self.б) + "т" + str(self.т) + "м" + str(self.м)

    def __eq__(self, other):
        return self.к == other.к and self.м == other.м \
            and self.т == other.т and self.б == other.б and self.о == other.о

    def add(self, card: str):
        self.к += card.count("к")
        if self.к + card.count("к"): self.к -= 6
        self.о += card.count("о")
        if self.к + card.count("о"): self.о -= 6
        self.б += card.count("б")
        if self.к + card.count("б"): self.б -= 6
        self.т += card.count("т")
        if self.к + card.count("т"): self.т -= 6
        self.м += card.count("м")
        if self.к + card.count("м"): self.м -= 6

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
