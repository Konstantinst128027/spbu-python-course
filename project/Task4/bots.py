from project.Task4.player import Player
from project.Task4.bet import Bet
import random
import typing


class External_bids_only_bot(Player):
    def __init__(self, initial_balance) -> None:
        """
        Creates a External_bids_only_bot
        Takes: initial balance
        """
        self.name: str = "External_bids_only_bot"
        super().__init__("External_bids_only_bot", initial_balance)

    def make_bet(self) -> Bet:
        """
        Creates bet according to External_bids_only_bot strategy
        Returns: bet
        """
        bet_value: typing.Union[str, int, typing.List[int]]

        bet = random.choice(["red_black", "even_odd", "less_more"])
        if bet == "red_black":
            bet_value = random.choice(["red", "black"])
        elif bet == "even_odd":
            bet_value = random.choice(["even", "odd"])
        else:
            bet_value = random.choice(["less", "more"])

        bet_amount = self.balance // 4
        self.bets.append((bet, bet_value, bet_amount))

        return Bet(bet, bet_value, bet_amount)


class Straight_only_bot(Player):
    def __init__(self, initial_balance) -> None:
        """
        Creates a Straight_only_bot
        Takes: initial balance
        """
        self.name: str = "Straight_only_bot"
        super().__init__("Straight_only_bot", initial_balance)

    def make_bet(self) -> Bet:
        """
        Creates bet according to Straight_only_bot strategy
        Returns: bet
        """
        bet_value: typing.Union[str, int, typing.List[int]]

        bet = "straight"
        bet_value = random.choice(range(37))

        bet_amount = self.balance // 6
        self.bets.append((bet, bet_value, bet_amount))

        return Bet(bet, bet_value, bet_amount)


class Random_bot(Player):
    def __init__(self, initial_balance) -> None:
        """
        Creates a Random_bot
        Takes: initial balance
        """
        self.name: str = "Random_bot"
        super().__init__("Random_bot", initial_balance)

    def make_bet(self) -> Bet:
        """
        Creates bet according to Random_bot strategy
        Returns: bet
        """
        bet_value: typing.Union[str, int, typing.List[int]]

        bet = random.choice(
            [
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
        )

        if bet == "red_black":
            bet_value = random.choice(["red", "black"])

        elif bet == "even_odd":
            bet_value = random.choice(["even", "odd"])

        elif bet == "less_more":
            bet_value = random.choice(["less", "more"])

        elif bet == "straight":
            bet_value = random.choice(range(37))

        elif bet == "split":
            first = random.choice(range(4, 33))

            if first % 3 == 0:
                second = random.choice([first - 1, first + 3, first - 3])

            elif first % 3 == 1:
                second = random.choice([first + 1, first + 3, first - 3])

            else:
                second = random.choice([first + 1, first + 3, first - 3, first - 1])

            bet_value = [first, second]

        elif bet == "street":
            bet_value = random.choice(range(1, 13))

        elif bet == "basket":
            bet_value = random.choice([[0, 1, 2], [0, 2, 3]])

        elif bet == "first_four":
            bet_value = [0, 1, 2, 3]

        elif bet == "corner":
            first = random.choice(range(1, 37))

            if first == 1:
                bet_value = [1, 2, 3, 4]

            elif first == 2:
                bet_value = random.choice([[2, 3, 5, 6], [1, 2, 4, 5]])

            elif first == 3:
                bet_value = [2, 3, 5, 6]

            elif first == 34:
                bet_value = [31, 32, 34, 35]

            elif first == 35:
                bet_value = random.choice([[31, 32, 34, 35], [32, 33, 35, 36]])

            elif first == 36:
                bet_value = [32, 33, 35, 36]

            elif first % 3 == 1:
                second = random.choice([-3, 3])
                bet_value = [first, first + 1, first + second, first + 1 + second]
            elif first % 3 == 0:
                second = random.choice([-3, 3])
                bet_value = [first, first - 1, first + second, first - 1 + second]
            elif first % 3 == 2:
                second = random.choice([-3, 3])
                third = random.choice([-1, 1])
                bet_value = [
                    first,
                    first + third,
                    first + second,
                    first + third + second,
                ]

        elif bet == "line":
            bet_value = random.choice(range(1, 7))

        elif bet == "column":
            bet_value = random.choice(range(1, 4))

        elif bet == "dozen":
            bet_value = random.choice(range(1, 4))

        bet_amount = self.balance // random.choice(range(1, 10))
        self.bets.append((bet, bet_value, bet_amount))

        return Bet(bet, bet_value, bet_amount)
