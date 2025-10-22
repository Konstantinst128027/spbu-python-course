import pytest
from project.Task4.roulet import Roulet
from project.Task4.bet import Bet


@pytest.fixture
def roulet():
    return Roulet()


def test_roulet_initialization(roulet):
    assert len(roulet.numbers) == 37
    assert roulet.numbers[0] == 0
    assert roulet.numbers[36] == 36
    assert len(roulet.red_numbers) == 18
    assert len(roulet.black_numbers) == 18


def test_spin_range(roulet):
    for _ in range(100):
        result = roulet.spin()
        assert result in range(37)


def test_get_color(roulet):

    assert roulet.get_color(0) == "green"

    for num in roulet.red_numbers:
        assert roulet.get_color(num) == "red"

    for num in roulet.black_numbers:
        assert roulet.get_color(num) == "black"


def test_is_even(roulet):

    assert roulet.is_even(2) == "even"
    assert roulet.is_even(3) == "odd"
    assert roulet.is_even(0) == "even"


def test_get_less_more(roulet):

    for num in range(1, 19):
        assert roulet.get_less_more(num) == "less"
    for num in range(19, 37):
        assert roulet.get_less_more(num) == "more"


@pytest.mark.parametrize(
    "bet_name,bet_value,winning_number,expected",
    [
        ("straight", 7, 7, 3500),
        ("straight", 7, 8, -100),
        ("split", [1, 2], 1, 1700),
        ("split", [1, 2], 3, -100),
        ("street", 1, 2, 1100),
        ("street", 1, 4, -100),
        ("line", 1, 3, 500),
        ("line", 1, 7, -100),
        ("dozen", 1, 5, 200),
        ("dozen", 1, 15, -100),
        ("column", 1, 4, 200),
        ("column", 1, 5, -100),
        ("corner", [1, 2, 4, 5], 2, 800),
        ("corner", [1, 2, 4, 5], 3, -100),
        ("basket", [0, 1, 2], 0, 1100),
        ("basket", [0, 1, 2], 3, -100),
        ("first_four", [0, 1, 2, 3], 2, 800),
        ("first_four", [0, 1, 2, 3], 4, -100),
        ("red_black", "red", 1, 100),
        ("red_black", "red", 2, -100),
        ("even_odd", "even", 2, 100),
        ("even_odd", "even", 3, -100),
        ("less_more", "less", 10, 100),
        ("less_more", "less", 20, -100),
    ],
)
def test_all_bet_types_parametrized(
    roulet, bet_name, bet_value, winning_number, expected
):
    """Test all 12 bet types with win/loss scenarios"""
    bet = Bet(bet_name, bet_value, 100)
    result = roulet.calculation_of_winning(bet, winning_number)
    assert result == expected
