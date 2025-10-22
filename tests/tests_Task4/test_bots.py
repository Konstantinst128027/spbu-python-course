import pytest
from project.Task4.bots import External_bids_only_bot, Straight_only_bot, Random_bot
from project.Task4.bet import Bet


@pytest.fixture
def ext_bot():
    return External_bids_only_bot(1000)


@pytest.fixture
def straight_bot():
    return Straight_only_bot(1000)


@pytest.fixture
def random_bot():
    return Random_bot(1000)


def test_external_bot_creation(ext_bot):
    assert ext_bot.name == "External_bids_only_bot"
    assert ext_bot.balance == 1000


def test_external_bot_make_bet(ext_bot):
    for i in range(50):
        bet = ext_bot.make_bet()

        assert bet.bet_name in ["red_black", "even_odd", "less_more"]
        assert isinstance(bet, Bet)
        assert bet.amount_of_money == 1000 // 4

        if bet.bet_name == "red_black":
            assert bet.value in ["red", "black"]
        elif bet.bet_name == "even_odd":
            assert bet.value in ["even", "odd"]
        elif bet.bet_name == "less_more":
            assert bet.value in ["less", "more"]


def test_straight_bot_creation(straight_bot):
    assert straight_bot.name == "Straight_only_bot"
    assert straight_bot.balance == 1000


def test_straight_bot_make_bet(straight_bot):
    for i in range(50):
        bet = straight_bot.make_bet()

        assert bet.bet_name == "straight"
        assert bet.value in range(37)
        assert bet.amount_of_money == 1000 // 6
        assert isinstance(bet, Bet)


def test_random_bot_creation(random_bot):
    assert random_bot.name == "Random_bot"
    assert random_bot.balance == 1000


def test_random_bot_make_bet_types(random_bot):
    valid_bet_types = [
        "red_black",
        "even_odd",
        "less_more",
        "straight",
        "split",
        "street",
        "basket",
        "first_four",
        "corner",
        "line",
        "dozen",
        "column",
    ]

    for i in range(100):
        bet = random_bot.make_bet()
        assert bet.bet_name in valid_bet_types
        assert isinstance(bet, Bet)
        assert bet.amount_of_money > 0
