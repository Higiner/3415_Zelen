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
        return ''.join(v * getattr(self, v) for v in self.vegetables)

    def __eq__(self, other):
        for v in self.vegetables:
            if getattr(self, v) != getattr(other, v):
                return False
        return True

    def score(self, price):
        total = 0
        for v in self.vegetables:
            total += getattr(self, v) * getattr(price, v)
        return total

    def save(self):
        return repr(self)

    @staticmethod
    def load(text: str):
        """From 'ттт' to Card(т=3)"""
        return Card(text.count("к"), text.count("о"), text.count("б"), text.count("т"), text.count("м"))

    @staticmethod
    def all_cards(vegetables: list[str] | None):
        if vegetables is None:
            vegetables = Card.vegetables
        cards = [Card.load(veg1 * 2 + veg2 * 1)  for veg1 in vegetables for veg2 in vegetables]
        cards += cards.copy()
        rm_card = [Card.load(veg * Const.max_veg.value) for veg in vegetables]
        for card in rm_card:
            cards.remove(card)
        return cards
