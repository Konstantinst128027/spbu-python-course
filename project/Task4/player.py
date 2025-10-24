import typing
import random
from project.Task4.bet import Bet


class Player:
    def __init__(self, name: str, initial_balance: int) -> None:
        """
        Creates a player
        Takes: name, initial balance
        """
        self.name: str = name
        self.balance: int = initial_balance
        self.bets: typing.List[typing.Tuple[str, typing.Any, int]] = []
        self.total_wins: int = 0
        self.total_losses: int = 0
        self.current_bet: typing.Optional[Bet] = None

    def make_bet(self) -> Bet:
        """
        Creates a bet
        Returns: bet object
        """
        amount = self.balance // 10
        return Bet(
            "red_black", "red", amount
        )  # default bet is simple, the method is not implemented for the player

    def is_bankrupt(self) -> bool:
        """
        Checks if player is bankrupt
        Takes: nothing
        Returns: True/False
        """
        if self.balance == 0:
            return True
        else:
            return False

    def adding_winnings(self, amount: int) -> None:
        """
        Adds winnings to balance
        Takes: amount
        """
        self.balance += amount
        if amount > 0:
            self.total_wins += 1
        else:
            self.total_losses += 1
