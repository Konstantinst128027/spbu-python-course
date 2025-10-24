import typing


class Bet:
    def __init__(self, name: str, value: typing.Any, amount_of_money: int) -> None:
        """
        Creates a bet
        Takes: bet type, value, amount
        """
        self.bet_name: str = name
        self.value: typing.Any = value
        self.amount_of_money: int = amount_of_money
