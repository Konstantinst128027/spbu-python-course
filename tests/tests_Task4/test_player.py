import pytest
from project.Task4.player import Player
from project.Task4.bet import Bet


@pytest.fixture
def player():
    return Player("TestPlayer", 1000)


def test_player_initialization(player):
    assert player.name == "TestPlayer"
    assert player.balance == 1000
    assert player.total_wins == 0
    assert player.total_losses == 0
    assert len(player.bets) == 0


def test_is_bankrupt(player):
    assert not player.is_bankrupt()

    bankrupt_player = Player("Bankrupt", 0)
    assert bankrupt_player.is_bankrupt()


def test_adding_winnings(player):
    initial_balance = player.balance
    player.adding_winnings(500)

    assert player.balance == initial_balance + 500
    assert player.total_wins == 1
    assert player.total_losses == 0

    player.adding_winnings(-300)

    assert player.balance == initial_balance + 500 - 300
    assert player.total_wins == 1
    assert player.total_losses == 1
