from src.card import Card
from src.hand import Hand
from src.price import Price


def test_init():
    h = Hand(1, 2, 3, 4, 5)
    assert h.к == 1
    assert h.о == 2
    assert h.б == 3
    assert h.т == 4
    assert h.м == 5

def test_save():
    h = Hand(3, 0, 2, 1)
    assert repr(h) == "к3о0б2т1м0"
    assert h.save() == "к3о0б2т1м0"

def test_load():
    t = "к4о2б3т0м1"
    assert Hand.load(t) == Price(4, 2, 3, 0, 1)

def test_add_card():
    h = Hand(3, 0, 2, 1)
    card = Card(к=2, м=1)
    h.add_card(card)
    assert  repr(h) == "к5о0б2т1м1"


def test_score():
    h = Hand(т=1, б=2)
    p = Price(1, 5, 3, 2, 4)
    assert h.score(p) == 2 + 2 * 3