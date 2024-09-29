import random

from src.card import Card


class Deck:
    def __init__(self, cards: None | list[Card]):
        if cards is None:
            cards = Card.all_cards()
            random.shuffle(cards)
        self.cards: list[Card] = cards

    def __repr__(self):
        return self.save()

    def full_deck(self, veg: str):
        rm_card = Card.all_cards(veg)
        for card in rm_card:
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
