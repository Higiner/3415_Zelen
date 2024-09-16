'''Карты Зелень'''

class Card:

    def __init__(self, к = 0, о = 0, б = 0, т = 0, м = 0):
        if к + о + б + т + м != 3:
            raise ValueError
        self.к = к
        self.о = о
        self.б = б
        self.т = т
        self.м = м

    def __repr__(self):
        return "к" * self.к + "о" * self.о + "б" * self.б + "т" * self.т + "м" * self.м

    def __eq__(self, other):
        return self.к == other.к and self.м == other.м \
            and self.т == other.т and self.б == other.б and self.о == other.о

    def score(self, other):
        return self.к * other.к + self.о * other.о + self.б * other.б + self.т * other.т + self.м * other.м

    def save(self):
        return repr(self)

    @staticmethod
    def load(text: str):
        """From 'ттт' to Card(т=3)"""
        return Card(text.count("к"), text.count("о"), text.count("б"), text.count("т"), text.count("м"))

