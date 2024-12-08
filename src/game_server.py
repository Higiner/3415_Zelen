import inspect
import enum
import json

from src.deck import Deck
from src.hand import Hand
from src.game_state import GameState
from src.player import Player
from src.price import Price
from src.player_interaction import PlayerInteraction
import src.player_interactions as all_player_types


class GamePhase(enum.StrEnum):
    NEW_ROND = "New round"
    CHOOSE_CARD = "Choose card"
    NEXT_PLAYER = "Switch current player"
    DECLARE_WINNER = "Declare a winner"
    GAME_END = "Game ended"

class GameServer:
    NROUNDS = 7

    def __init__(self, player_types, game_state):
        self.game_state = game_state
        self.player_types = player_types

    @classmethod
    def load_game(cls):
        filename = 'zelen.json'
        with open(filename, 'r', encoding='utf-8') as fin:
            data = json.load(fin)
            game_state = GameState.load(data)
            print(game_state.save())
            player_types = {}
            for player, player_data in zip(game_state.players, data['players']):
                kind = player_data['kind']
                kind = getattr(all_player_types, kind)
                player_types[player] = kind
            return GameServer(player_types=player_types, game_state=game_state)

    @classmethod
    def new_game(cls):
        player_count = cls.request_player_count()

        player_types = {}
        for p in range(player_count):
            name, kind = cls.request_player()
            player = Player(name, Hand())
            player_types[player] = kind

        deck = Deck(cards=None)
        price = Price()
        cards = []
        for _ in range(player_count + 1):
            cards.append(deck.draw_card())
        game_state = GameState(list(player_types.keys()), deck, price, cards)

        print(game_state.save())

        res = cls(player_types, game_state)
        return res

    def run(self):
        current_phase = GamePhase.CHOOSE_CARD
        while current_phase != GamePhase.GAME_END:
            phases = {
                GamePhase.NEW_ROND: self.new_round,
                GamePhase.CHOOSE_CARD: self.choose_card_phase,
                GamePhase.NEXT_PLAYER: self.next_player_phase,
                GamePhase.DECLARE_WINNER: self.declare_winner_phase,
            }
            current_phase = phases[current_phase]()

    def new_round(self) -> GamePhase:
        self.game_state.price.add(self.game_state.cards[0].save())
        self.game_state.cards.pop()
        for _ in range(len(self.game_state.players) + 1):
            self.game_state.cards.append(self.game_state.deck.draw_card())
        self.game_state.nround += 1
        return GamePhase.NEXT_PLAYER

    def choose_card_phase(self) -> GamePhase:
        print(f"Round {self.game_state.nround}")
        print(f"Price {self.game_state.price.save()}")
        for card in self.game_state.cards:
            print(f"{self.game_state.cards.index(card) + 1}){card}")
        current_player = self.game_state.current_player()
        card = self.player_types[current_player].choose_card(
            self.game_state.price, self.game_state.cards
        )
        current_player.hand.add_card(card)
        self.game_state.cards.remove(card)
        return GamePhase.NEXT_PLAYER

    def next_player_phase(self) -> GamePhase:
        if self.game_state.nround == self.NROUNDS:
            return GamePhase.DECLARE_WINNER
        if len(self.game_state.cards) == 1:
            return GamePhase.NEW_ROND
        self.game_state.next_player()
        print(f"=== {self.game_state.current_player()}'s turn")
        return GamePhase.CHOOSE_CARD

    def declare_winner_phase(self) -> GamePhase:
        winner = max(self.game_state.players, key= lambda player: player.hand.score(self.game_state.price))
        print(f"{winner.name} is the winner!")
        return GamePhase.GAME_END

    @staticmethod
    def request_player_count() -> int:
        while True:
            try:
                player_count = int(input("How many players?" ))
                if 2 <= player_count <= 6:
                    return player_count
            except ValueError:
                pass
            print("Please input a number between 2 and 6")

    @staticmethod
    def request_player() -> (str, PlayerInteraction):
        while True:
            name = input("How to call a player? ")
            if name.isalpha():
                break
            print("Name must be a single word, alphabetic characters only")

        while True:
            try:
                kind = input("What kind of player is it (Bot, Human, etc.)? ")
                kind = getattr(all_player_types, kind)
                break
            except AttributeError:
                options = []
                for name, cls in inspect.getmembers(all_player_types):
                    if inspect.isclass(cls) and issubclass(cls, PlayerInteraction):
                        options.append(cls.__name__)
                print(f"Allowed player types are: {', '.join(options)}")
        return name, kind

def __main__():
    try:
        server = GameServer.load_game()
    except:
        server = GameServer.new_game()
    server.run()

if __name__ == "__main__":
    __main__()
