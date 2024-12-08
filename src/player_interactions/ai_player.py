from src.card import Card
from src.price import Price
from src.player import Player

from src.player_interaction import PlayerInteraction

class Bot(PlayerInteraction):
    @classmethod
    def choose_card(
            cls, price : Price, cards: list[Card]
    ) -> Card:
        best_card = max(cards, key=lambda card: card.score(price) )
        return best_card

    @classmethod
    def inform_card_drawn(cls, player: Player):
        pass
