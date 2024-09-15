import pytest

from src.card import Card

def test_init():
    c = Card(corn=2, carrot=1)
    assert c.Corn == 2
    assert c.Carrot == 1

def test_validation():
    with pytest.raises(ValueError):
        Card(tomato=4)
        Card(tomato=1, eggplant=1, carrot=1, corn=1)

def test_save():
    c = Card(tomato=1, eggplant=2)
    assert repr(c) == "Eggplant - 2; Tomato - 1"
    assert c.save() == "Eggplant - 2; Tomato - 1"

def test_load():
    t = "Tomato - 3"
    c = Card.load(t)
    assert c == Card(tomato=3)
