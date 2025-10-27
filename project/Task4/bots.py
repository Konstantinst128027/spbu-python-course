from project.Task4.player import Player
from project.Task4.bet import Bet
from enum import Enum
import random
import typing


class External_bids_only_bot(Player):
    def __init__(self, initial_balance: int) -> None:
        """
        Creates a External_bids_only_bot
        Takes: initial balance
        """
        self.name: str = "External_bids_only_bot"
        super().__init__("External_bids_only_bot", initial_balance)

    class BetType(Enum):
        RED_BLACK = "red_black"
        EVEN_ODD = "even_odd"
        LESS_MORE = "less_more"

    def make_bet(self) -> Bet:
        """
        Creates bet according to External_bids_only_bot strategy
        Returns: bet
        """
        bet_value: typing.Union[str, int, typing.List[int]]

        bet = random.choice(list(self.BetType))

        if bet == self.BetType.RED_BLACK:
            bet_value = random.choice(["red", "black"])
        elif bet == self.BetType.EVEN_ODD:
            bet_value = random.choice(["even", "odd"])
        else:
            bet_value = random.choice(["less", "more"])

        bet_amount = self.balance // 4
        self.bets.append((bet.value, bet_value, bet_amount))

        return Bet(bet.value, bet_value, bet_amount)


class Straight_only_bot(Player):
    def __init__(self, initial_balance: int) -> None:
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
        bet_value = random.randint(0, 36)

        bet_amount = self.balance // 6
        self.bets.append((bet, bet_value, bet_amount))

        return Bet(bet, bet_value, bet_amount)


class Random_bot(Player):
    def __init__(self, initial_balance: int) -> None:
        """
        Creates a Random_bot
        Takes: initial balance
        """
        self.name: str = "Random_bot"
        super().__init__("Random_bot", initial_balance)

    class BetType(Enum):
        RED_BLACK = "red_black"
        EVEN_ODD = "even_odd"
        LESS_MORE = "less_more"
        STRAIGHT = "straight"
        SPLIT = "split"
        STREET = "street"
        BASKET = "basket"
        FIRST_FOUR = "first_four"
        CORNER = "corner"
        LINE = "line"
        COLUMN = "column"
        DOZEN = "dozen"

    def make_bet(self) -> Bet:
        """
        Creates bet according to Random_bot strategy
        Returns: bet
        """
        bet_value: typing.Union[str, int, typing.List[int]]

        bet = random.choice(list(self.BetType))

        if bet == self.BetType.RED_BLACK:
            bet_value = random.choice(["red", "black"])

        elif bet == self.BetType.EVEN_ODD:
            bet_value = random.choice(["even", "odd"])

        elif bet == self.BetType.LESS_MORE:
            bet_value = random.choice(["less", "more"])

        elif bet == self.BetType.STRAIGHT:
            bet_value = random.randint(0, 36)

        elif bet == self.BetType.SPLIT:
            first = random.randint(4, 33)
            if first % 3 == 0:
                second = random.choice([first - 1, first + 3, first - 3])
            elif first % 3 == 1:
                second = random.choice([first + 1, first + 3, first - 3])
            else:
                second = random.choice([first + 1, first + 3, first - 3, first - 1])
            bet_value = [first, second]

        elif bet == self.BetType.STREET:
            bet_value = random.randint(1, 13)

        elif bet == self.BetType.BASKET:
            bet_value = random.choice([[0, 1, 2], [0, 2, 3]])

        elif bet == self.BetType.FIRST_FOUR:
            bet_value = [0, 1, 2, 3]

        elif bet == self.BetType.CORNER:
            first = random.randint(1, 36)
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
            else:
                if first % 3 == 1:
                    second = random.choice([-3, 3])
                    bet_value = [
                        first,
                        first + 1,
                        first + second,
                        first + 1 + second,
                    ]
                elif first % 3 == 0:
                    second = random.choice([-3, 3])
                    bet_value = [
                        first,
                        first - 1,
                        first + second,
                        first - 1 + second,
                    ]
                else:
                    second = random.choice([-3, 3])
                    third = random.choice([-1, 1])
                    bet_value = [
                        first,
                        first + third,
                        first + second,
                        first + third + second,
                    ]

        elif bet == self.BetType.LINE:
            bet_value = random.randint(1, 7)

        elif bet == self.BetType.COLUMN:
            bet_value = random.randint(1, 4)

        elif bet == self.BetType.DOZEN:
            bet_value = random.randint(1, 4)

        bet_amount = self.balance // random.randint(1, 10)
        self.bets.append((bet.value, bet_value, bet_amount))

        return Bet(bet.value, bet_value, bet_amount)


class Martingale_bot(Player):
    def __init__(self, initial_balance: int) -> None:
        """
        Creates a Martingale_bot
        Takes: initial balance
        """
        self.name: str = "Martingale_bot"
        super().__init__(self.name, initial_balance)
        self.base_bet = 100  # basic bet
        self.current_bet_amount = self.base_bet
        self.last_bet_won = True
        self.consecutive_losses = 0

    def make_bet(self) -> Bet:
        """
        Creates bet according to Martingale strategy
        Returns: bet
        """
        if self.last_bet_won:
            self.current_bet_amount = self.base_bet
            self.consecutive_losses = 0
        else:
            self.current_bet_amount = min(self.current_bet_amount * 2, self.balance)
            self.consecutive_losses += 1

        bet_type = "red_black"
        bet_value = random.choice(["red", "black"])

        if self.current_bet_amount > self.balance:
            self.current_bet_amount = self.balance

        bet_amount = self.current_bet_amount

        self.bets.append((bet_type, bet_value, bet_amount))

        return Bet(bet_type, bet_value, bet_amount)

    def adding_winnings(self, winnings: int) -> None:
        """
        Updates balance and tracks win/loss for Martingale strategy
        """
        super().adding_winnings(winnings)

        if winnings > 0:
            self.last_bet_won = True
        else:
            self.last_bet_won = False
