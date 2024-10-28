import inspect
from random import randint

from src.deck import Deck
from src.hand import Hand
from src.game_state import GameState
from src.player import Player
import enum


from src.price import Price


class GamePhase(enum.StrEnum):
    CHOOSE_CARD = "Choose card"
    NEXT_PLAYER = "Switch current player"
    DECLARE_WINNER = "Declare a winner"
    GAME_END = "Game ended"

class GameServer:
    def __init__(self, player_types, game_state):
        self.game_state = game_state
        self.player_types = player_types

    @classmethod
    def load_game(cls):
        pass

    def new_game(cls):
        player_count = cls.request_player_count()

        player_types = {}
        for p in range(player_count):
            name, kind = cls.request_player()
            player = Player(name, Hand())
            player_types[player] = kind

        deck = Deck(cards=None)
        for veg in ['к', 'о', 'б', 'т', 'м']:
            veg = randint
        price = Price()
        game_state = GameState(list(player_types.keys()), deck, price)

    def run(self):
        current_phase = GamePhase.CHOOSE_CARD
        while current_phase != GamePhase.GAME_END:
            phases = {
                GamePhase.CHOOSE_CARD: self.choose_card_phase,
                GamePhase.NEXT_PLAYER: self.next_player_phase,
                GamePhase.DECLARE_WINNER: self.declare_winner_phase,
            }
            current_phase = phases[current_phase]()

    def choose_card_phase(self) -> GamePhase:
        pass

    def next_player_phase(self) -> GamePhase:
        if self.game_state.nround == 6:
            return GamePhase.DECLARE_WINNER
        self.game_state.next_player()
        print(f"=== {self.game_state.current_player()}'s turn")
        return GamePhase.CHOOSE_CARD

    def declare_winner_phase(self) -> GamePhase:
        max_score = 0
        winner = None
        for player in self.game_state.players:
            if player.hande.score > max_score:
                max_score = player.hande.score
                winner = player
        print(f"{winner.name} is the winner!")
        return GamePhase.GAME_END

    @staticmethod
    def request_player_count() -> int:
        pass


def __main__():
    server = GameServer.new_game()
    server.run()


if __name__ == "__main__":
    __main__()
