import pytest
from project.Task4.bet import Bet


def test_bet_creation():
    """Test Bet creation with different parameters"""
    bet = Bet("straight", 7, 100)
    assert bet.bet_name == "straight"
    assert bet.value == 7
    assert bet.amount_of_money == 100


def test_bet_different_types():
    """Test Bet with different value types"""
    # Test with list value (for split bet)
    split_bet = Bet("split", [1, 2], 50)
    assert split_bet.value == [1, 2]

    # Test with string value (for color bet)
    color_bet = Bet("red_black", "red", 75)
    assert color_bet.value == "red"


def test_bet_amount_negative():
    """Test Bet with negative amount"""
    bet = Bet("straight", 5, -100)
    assert bet.amount_of_money == -100
