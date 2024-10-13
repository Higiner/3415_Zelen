from src.deck import Deck
from src.player import Player
from src.price import Price

class GameState:
    def __init__(self, players: list[Player], deck: Deck, price: Price, current_player: int = 0, nround: int = 1):
        self.players: list[Player] = players
        self.deck: Deck = deck
        self._current_player: int = current_player
        self.price = price
        self.nround = nround


    def current_player(self) -> Player:
        return self.players[self._current_player]

    def __eq__(self, other):
        if self.players != other.players:
            return False
        if self.deck != other.deck:
            return False
        if self._current_player != other._current_player:
            return False
        if self.price != other.price:
            return False
        if self.nround != other.nround:
            return False
        return True

    def save(self):
        return {
            "Price": str(self.price),
            "Deck":str(self.deck),
            "Round": self.nround,
            "current_player_index": self._current_player,
            "players": [p.save() for p in self.players]
        }

    @classmethod
    def load(cls, data: dict):
        players = [Player.load(d) for d in data["players"]]

        return cls(
            players=players,
            deck=Deck.load(data["Deck"]),
            price=Price.load(data["Price"]),
            current_player=int(data["current_player_index"]),
            nround=int(data["Round"])
        )

    def next_player(self):
        """Ход переходит к следующему игроку."""
        n = len(self.players)
        self._current_player = (self._current_player + 1) % n
