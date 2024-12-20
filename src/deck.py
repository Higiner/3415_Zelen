import random

from src.card import Card
from src.const import Const


class Deck:
    def __init__(self, cards: None | list[Card]):
        if cards is None:
            cards = Card.all_cards(None)
            random.shuffle(cards)
        self.cards: list[Card] = cards

    def __repr__(self):
        return self.save()

    def remove_veg(self, veg: str):
        self.cards.remove(Card.load(veg*Const.max_veg.value))
        for card in self.cards:
            if veg in repr(card):
                self.cards.remove(card)
                self.cards.remove(card)

    def save(self):
        scards = [c.save() for c in self.cards]
        s = ' '.join(scards)
        return s

    @classmethod
    def load(cls, text: str):
        """Преобразует 'ббб ббм бмм ммм' """
        cards = [Card.load(s) for s in text.split()]
        return cls(cards=cards)

    def draw_card(self):
        """Берем карту из колоды и возвращаем ее."""
        return self.cards.pop()

    def shuffle(self):
        random.shuffle(self.cards)
