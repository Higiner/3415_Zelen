import pytest

from src.card import Card
from src.price import Price


def test_init():
    c = Card(к=2, м=1)
    assert c.к == 2
    assert c.м == 1

def test_validation():
    with pytest.raises(ValueError):
        Card(т=4)
        Card(т=1, о=1, м=1, к=1)

def test_save():
    c = Card(т=1, о=2)
    assert repr(c) == "оот"
    assert c.save() == "оот"

def test_load():
    t = "ттт"
    c = Card.load(t)
    assert c == Card(т=3)

def test_score():
    c = Card(т=1, б=2)
    p = Price(1, 5, 3, 2, 4)
    assert c.score(p) == 2 + 2 * 3