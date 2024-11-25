from abc import ABC, abstractmethod

from src.card import Card
from src.price import Price
from src.player import Player


class PlayerInteraction(ABC):
    @classmethod
    @abstractmethod
    def choose_card(
            cls, price : Price, cards: list[Card]) -> Card:
        pass

    @classmethod
    def inform_card_drawn(cls, player: Player):
        pass
