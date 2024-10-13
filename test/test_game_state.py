from src.card import Card
from src.deck import Deck
from src.player import Player
from src.price import Price
from src.game_state import GameState


data = {
    "Price": "к4о2б3т0м1",
    "Deck": "ббм бмм ббб ббм бмм ммм",
    "Round": 1,
    "current_player_index": 1,
    "players": [
        {"name": "Alex", "hand": "к1о0б4т1м1", "score": 10},
        {"name": "Bob", "hand": "к1о0б2т3м1", "score": 7}
    ]
}

alex = Player.load(data["players"][0])
bob = Player.load(data["players"][1])
full_deck = Deck(None)
price = Price.load("к4о2б3т0м1")

def test_init():
    players = [alex, bob]
    game = GameState(players=players, deck=full_deck, price=price, current_player=0, nround=1)
    assert  game.players == players
    assert game.deck == full_deck
    assert game.price == price
    assert game._current_player == 0
    assert game.nround ==1

def test_current_players():
    players = [alex, bob]
    game = GameState(players=players, deck=full_deck, price=price, nround=1)
    assert game.current_player() == alex
    game = GameState(players=players, deck=full_deck, price=price, current_player=1, nround=1)
    assert game.current_player() == bob

def test_eq():
    players = [alex, bob]
    game1 = GameState(players=players, deck=full_deck, price=price, current_player=1, nround=1)
    game2 = GameState(players=players.copy(), deck=full_deck, price=price, current_player=1, nround=1)
    game3 = GameState(
        players=players, deck=Deck(Card.all_cards(["б", "м"])), price=price, current_player=1, nround=1
    )
    assert game1 == game2
    assert game1 != game3

def test_save():
    players = [alex, bob]
    game = GameState(players=players, deck=Deck(Card.all_cards(["б", "м"])), price=price, current_player=1, nround=1)
    assert game.save() == data

def test_load():
    game = GameState.load(data)
    assert game.save() == data

def test_next_player():
    game = GameState.load(data)
    assert str(game.current_player()) == str(bob)

    game.next_player()
    assert str(game.current_player()) == str(alex)

    game.next_player()
    assert str(game.current_player()) == str(bob)


