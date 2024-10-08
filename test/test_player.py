from src.hand import Hand
from src.player import Player

def test_init():
    h = Hand(1, 2, 3, 4, 5)
    p = Player(name='Alex', hand=h, score=15)
    assert p.name == 'Alex'
    assert p.hand == h
    assert p.score == 15

def test_load():
    d = {'hand': 'к1о2б3т4м5', 'name': 'Alex', 'score': 15}
    h_e = Hand(1, 2, 3, 4, 5)
    p_e = Player(name='Alex', hand=h_e, score=15)
    assert str(p_e) == str(Player.load(d))

def test_save():
    h = Hand(1, 2, 3, 4, 5)
    p = Player(name='Alex', hand=h, score=15)
    assert str(p) == "Alex(15): к1о2б3т4м5"
    assert p.save() == {'hand': 'к1о2б3т4м5', 'name': 'Alex', 'score': 15}
