import typing
from project.Task4.roulet import Roulet
from project.Task4.player import Player
from project.Task4.bet import Bet
from project.Task4.print_in_txt import print_in_txt


class Move:
    def __init__(self, player: typing.List[Player], roulet: Roulet) -> None:
        """
        Creates a move round
        Takes: List of bots (each has current_bet), roulette
        """
        self.player: typing.List[Player] = player
        self.roulet: Roulet = roulet

    def displaying_information(self, winning_number: int) -> None:
        """
        Displays round information
        Takes: winning number
        """
        print_in_txt(
            f"\nWinning number is {winning_number} - {self.roulet.get_color(winning_number)}, {self.roulet.is_even(winning_number)}, {self.roulet.get_less_more(winning_number)}\n"
        )
        for bot in self.player:
                if bot.current_bet is not None:
                    print_in_txt(
                        f"{bot.name} - {bot.balance}, bet: {bot.current_bet.bet_name} - {bot.current_bet.value} - {bot.current_bet.amount_of_money}, {bot.total_wins}/{bot.total_losses}"
                    )

    def round(self, winning_number: int) -> None:
        """
        Processes a game round
        Takes: winning number
        """
        for bot in self.player:
            if bot.current_bet is not None:
                winning = self.roulet.calculation_of_winning(
                    bot.current_bet, winning_number
                )
                bot.adding_winnings(winning)
