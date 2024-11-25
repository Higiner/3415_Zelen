from src.card import Card
from src.price import Price
from src.player import Player

from src.player_interaction import PlayerInteraction

class Bot(PlayerInteraction):
    @classmethod
    def choose_card(
            cls, price : Price, cards: list[Card]
    ) -> Card:
        best_card_price = 0
        best_card = None
        for card in cards:
            if card.score(price) > best_card_price:
                best_card_price = card.score(price)
                best_card = card
        return best_card

    @classmethod
    def inform_card_drawn(cls, player: Player):
        pass
