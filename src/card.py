'''Карты Зелень'''
from src.const import Const


class Card:
    vegetables = ['к', 'о', 'б', 'т', 'м']

    def __init__(self, к = None, о = None, б= None, т = None, м = None):
        if к is None: к = 0
        if о is None: о = 0
        if б is None: б = 0
        if т is None: т = 0
        if м is None: м = 0
        if к + о + б + т + м != Const.max_veg.value:
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

    def score(self, price):
        return self.к * price.к + self.о * price.о + self.б * price.б + self.т * price.т + self.м * price.м

    def save(self):
        return repr(self)

    @staticmethod
    def load(text: str):
        """From 'ттт' to Card(т=3)"""
        return Card(text.count("к"), text.count("о"), text.count("б"), text.count("т"), text.count("м"))

    @staticmethod
    def all_cards(vegetables: list[str] | None = None):
        if vegetables is None:
            vegetables = Card.vegetables + Card.vegetables
        cards = [Card.load(veg1 * 2 + veg2 * 1)  for veg1 in vegetables for veg2 in vegetables]
        cards += cards.copy()
        rm_card = [Card.load(veg * Const.max_veg.value) for veg in vegetables]
        for card in rm_card:
            cards.remove(card)
        return cards
