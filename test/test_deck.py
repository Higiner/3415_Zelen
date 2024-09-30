import random

from src.card import Card
from src.deck import Deck

cards = [Card.load('ббм'), Card.load('бмм'), Card.load('ббб')]

def test_init():
    deck = Deck(cards)
    assert deck.cards == cards

def test_init_shuffle():
    full_deck1 = Deck(None)
    full_deck2 = Deck(None)
    assert full_deck1.cards != full_deck2.cards

def test_save():
    deck = Deck(cards=cards)
    assert deck.save() == "ббм бмм ббб"

def test_load():
    deck = Deck.load("ббм бмм ббб")
    expected_deck = Deck(cards)
    assert str(deck) == str(expected_deck)

def test_draw_card():
    deck1 = Deck.load("ббм бмм ббб")
    deck2 = Deck.load("ббм бмм")
    card = deck1.draw_card()
    assert card == Card.load('ббб')
    assert str(deck1) == str(deck2)

def test_shuflle():
    cards = Card.all_cards(['б', 'м'])
    deck = Deck(cards=cards)
    deck_list = [deck.save()]
    for i in range(5):
        deck.shuffle()
        s = deck.save()
        assert s not in deck_list
        deck_list.append(s)

def test_remove_veg():
    cards = Card.all_cards(['б', 'м', 'к'])
    deck = Deck(cards=cards)
    deck.remove_veg('к')
    cards_e = Card.all_cards(['б', 'м', 'к'])
    deck_e = Deck(cards=cards)
    assert deck_e.save() == deck.save()
