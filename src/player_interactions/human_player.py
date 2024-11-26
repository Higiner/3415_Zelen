from src.card import Card
from src.price import Price
from src.player import Player

from src.player_interaction import PlayerInteraction

class Human(PlayerInteraction):
    @classmethod
    def choose_card(
            cls, price: Price, cards: list[Card]
    ) -> Card:
        while True:
            numb = input('Выберите карту ')
            try:
                card = Card.load(numb)
                if card in cards:
                    return card
                else:
                    print('Нельзя взять эту карту')
            except ValueError:
                print('Polzuites russkoi rascladcoi')

    @classmethod
    def inform_card_drawn(cls, player: Player):
        pass
