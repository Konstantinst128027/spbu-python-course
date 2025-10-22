import typing
from project.Task4.roulet import Roulet
from project.Task4.player import Player
from project.Task4.bet import Bet


class Move:
    def __init__(self, bets: typing.Dict[Player, Bet], roulet: Roulet) -> None:
        """
        Creates a move round
        Takes: Dict - players_bets, roulette
        """
        self.bets: typing.Dict[Player, Bet] = bets
        self.roulet: Roulet = roulet

    def displaying_information(self, winning_number: int) -> None:
        """
        Displays round information
        Takes: winning number
        """
        print(
            f"Winning number is {winning_number} - {self.roulet.get_color(winning_number)}, {self.roulet.is_even(winning_number)}, {self.roulet.get_less_more(winning_number)}\n"
        )

        for key_1, value in self.bets.items():
            print(
                f"{key_1.name} - {key_1.balance}, bet: {value.bet_name} - {value.value} - {value.amount_of_money}, {key_1.total_wins}/{key_1.total_losses}"
            )

    def round(self, winning_number: int) -> None:
        """
        Processes a game round
        Takes: winning number
        """
        winning = []
        i = 0
        for key, value in self.bets.items():
            winning.append(self.roulet.calculation_of_winning(value, winning_number))
            key.adding_winnings(winning[i])
            i += 1
