import pytest

from src.price import Price

def test_init():
    p = Price(0, 1, 2, 3)
    assert p.к == 0
    assert p.о == 1
    assert p.б == 2
    assert p.т == 3
    p1 = Price()
    p2 = Price()
    assert p1 != p2

def test_validation():
    with pytest.raises(ValueError):
        p = Price(1, 3, 4, 7)

def test_save():
    p = Price(3, 0, 2, 1)
    assert repr(p) == "к3о0б2т1м0"
    assert p.save() == "к3о0б2т1м0"

def test_load():
    t = "к4о2б3т0м1"
    assert Price.load(t) == Price(4, 2, 3, 0, 1)

def test_add():
    p = Price(5, 0, 2, 1)
    p.add("кко")
    assert p.к == p.о == 1
