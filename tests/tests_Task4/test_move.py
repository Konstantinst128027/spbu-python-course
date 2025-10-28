import pytest
from project.Task4.move import Move
from project.Task4.bots import External_bids_only_bot, Straight_only_bot, Random_bot
from project.Task4.roulet import Roulet
from project.Task4.bet import Bet


@pytest.fixture
def setup_move():
    roulet = Roulet()
    ext_bot = External_bids_only_bot(1000)
    straight_bot = Straight_only_bot(1000)
    random_bot = Random_bot(1000)

    ext_bot.current_bet = ext_bot.make_bet()
    straight_bot.current_bet = straight_bot.make_bet()
    random_bot.current_bet = random_bot.make_bet()

    player = [ext_bot, straight_bot, random_bot]

    move = Move(player, roulet)
    return move, player, roulet


def test_move_initialization(setup_move):
    move, player, roulet = setup_move
    assert move.player == player
    assert move.roulet == roulet


def test_round_execution(setup_move):
    move, player, roulet = setup_move
    initial_balances = {bot: bot.balance for bot in player}

    winning_number = roulet.spin()
    move.round(winning_number)

    for bot in player:
        assert bot.balance != initial_balances[bot]


def test_round_external_bot_win(setup_move):
    move, player, roulet = setup_move

    for bot in player:
        if bot.name == "External_bids_only_bot":
            ext_bot = bot
            break

    ext_bot.current_bet = ext_bot.make_bet()
    winning_number = roulet.red_numbers[0]

    initial_balance = ext_bot.balance
    move.round(winning_number)

    assert ext_bot.balance != initial_balance
    assert ext_bot.total_wins + ext_bot.total_losses == 1


def test_round_straight_bot_win(setup_move):
    move, player, roulet = setup_move

    for bot in player:
        if bot.name == "Straight_only_bot":
            straight_bot = bot
            break

    straight_bot.current_bet = straight_bot.make_bet()
    winning_number = 7

    initial_balance = straight_bot.balance
    move.round(winning_number)

    assert straight_bot.balance != initial_balance
    assert straight_bot.total_wins + straight_bot.total_losses == 1


def test_round_random_bot_win(setup_move):
    move, player, roulet = setup_move

    for bot in player:
        if bot.name == "Random_bot":
            random_bot = bot
            break

    random_bot.current_bet = random_bot.make_bet()
    winning_number = roulet.spin()

    initial_balance = random_bot.balance
    move.round(winning_number)

    assert random_bot.balance != initial_balance
    assert random_bot.total_wins + random_bot.total_losses == 1
