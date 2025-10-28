import typing
import random
from enum import Enum
from project.Task4.bet import Bet
from project.Task4.print_in_txt import print_in_txt


class Roulet:
    class BetType(Enum):
        STRAIGHT = "straight"
        SPLIT = "split"
        STREET = "street"
        BASKET = "basket"
        FIRST_FOUR = "first_four"
        CORNER = "corner"
        LINE = "line"
        RED_BLACK = "red_black"
        EVEN_ODD = "even_odd"
        DOZEN = "dozen"
        COLUMN = "column"
        LESS_MORE = "less_more"

    class ColorType(Enum):
        RED = "red"
        BLACK = "black"
        GREEN = "green"

    class ParityType(Enum):
        EVEN = "even"
        ODD = "odd"

    class RangeType(Enum):
        LESS = "less"
        MORE = "more"

    def __init__(self) -> None:
        """
        Initializes the roulette wheel
        """
        self.numbers: typing.List[int] = list(range(37))
        self.red_numbers: typing.List[int] = [
            1,
            3,
            5,
            7,
            9,
            12,
            14,
            16,
            18,
            19,
            21,
            23,
            25,
            27,
            30,
            32,
            34,
            36,
        ]
        self.black_numbers: typing.List[int] = [
            2,
            4,
            6,
            8,
            10,
            11,
            13,
            15,
            17,
            20,
            22,
            24,
            26,
            28,
            29,
            31,
            33,
            35,
        ]
        self.coefficients: typing.Dict[typing.Any, int] = {
            self.BetType.STRAIGHT: 35,
            self.BetType.SPLIT: 17,
            self.BetType.STREET: 11,
            self.BetType.BASKET: 11,
            self.BetType.FIRST_FOUR: 8,
            self.BetType.CORNER: 8,
            self.BetType.LINE: 5,
            self.BetType.RED_BLACK: 1,
            self.BetType.EVEN_ODD: 1,
            self.BetType.DOZEN: 2,
            self.BetType.COLUMN: 2,
            self.BetType.LESS_MORE: 1,
        }

    def spin(self) -> int:
        """
        Spins the roulette wheel
        """
        return random.randint(0, 36)

    def get_red_number(self) -> None:
        """
        Displays red numbers
        """
        print_in_txt(f"red_numbers: {self.red_numbers}")

    def get_black_number(self) -> None:
        """
        Displays black numbers
        """
        print_in_txt(f"black_numbers: {self.black_numbers}")

    def displaying_name_of_bets(self) -> None:
        """
        Displays available bet types
        """
        for key, value in self.coefficients.items():
            print_in_txt(f"name: {key.value}, coefficients: {value}")

    def get_color(self, number: int) -> str:
        """
        Determines number color
        Takes: number
        Returns: color
        """
        if number == 0:
            return self.ColorType.GREEN.value
        elif number in self.red_numbers:
            return self.ColorType.RED.value
        else:
            return self.ColorType.BLACK.value

    def is_even(self, number: int) -> str:
        """
        Checks if number is even
        Takes: number
        Returns: 'even' or 'odd'
        """
        if number % 2 == 0:
            return self.ParityType.EVEN.value
        else:
            return self.ParityType.ODD.value

    def get_less_more(self, number: int) -> str:
        """
        Determines number range
        Takes: number
        Returns: 'less' or 'more'
        """
        if number <= 18:
            return self.RangeType.LESS.value
        else:
            return self.RangeType.MORE.value

    def calculation_of_winning(self, bet: Bet, winning_number: int) -> int:
        """
        Calculates bet winnings
        Takes: bet, winning number
        Returns: amount
        """
        if bet.bet_name == self.BetType.STRAIGHT.value:
            if winning_number == bet.value:
                return self.coefficients[self.BetType.STRAIGHT] * bet.amount_of_money
            else:
                return -bet.amount_of_money

        elif bet.bet_name == self.BetType.SPLIT.value:
            if winning_number in bet.value:
                return self.coefficients[self.BetType.SPLIT] * bet.amount_of_money
            else:
                return -bet.amount_of_money

        elif bet.bet_name == self.BetType.STREET.value:
            if (
                winning_number
                in self.numbers[(bet.value - 1) * 3 + 1 : bet.value * 3 + 1]
            ):
                return self.coefficients[self.BetType.STREET] * bet.amount_of_money
            else:
                return -bet.amount_of_money

        elif bet.bet_name == self.BetType.LINE.value:
            if (
                winning_number
                in self.numbers[(bet.value - 1) * 6 + 1 : bet.value * 6 + 1]
            ):
                return self.coefficients[self.BetType.LINE] * bet.amount_of_money
            else:
                return -bet.amount_of_money

        elif bet.bet_name == self.BetType.DOZEN.value:
            if (
                winning_number
                in self.numbers[(bet.value - 1) * 12 + 1 : bet.value * 12 + 1]
            ):
                return self.coefficients[self.BetType.DOZEN] * bet.amount_of_money
            else:
                return -bet.amount_of_money

        elif bet.bet_name == self.BetType.COLUMN.value:
            if winning_number in self.numbers[bet.value :: 3]:
                return self.coefficients[self.BetType.COLUMN] * bet.amount_of_money
            else:
                return -bet.amount_of_money

        elif bet.bet_name == self.BetType.CORNER.value:
            if winning_number in bet.value:
                return self.coefficients[self.BetType.CORNER] * bet.amount_of_money
            else:
                return -bet.amount_of_money

        elif bet.bet_name == self.BetType.RED_BLACK.value:
            if self.get_color(winning_number) == bet.value:
                return self.coefficients[self.BetType.RED_BLACK] * bet.amount_of_money
            else:
                return -bet.amount_of_money

        elif bet.bet_name == self.BetType.EVEN_ODD.value:
            if self.is_even(winning_number) == bet.value:
                return self.coefficients[self.BetType.EVEN_ODD] * bet.amount_of_money
            else:
                return -bet.amount_of_money

        elif bet.bet_name == self.BetType.LESS_MORE.value:
            if self.get_less_more(winning_number) == bet.value:
                return self.coefficients[self.BetType.LESS_MORE] * bet.amount_of_money
            else:
                return -bet.amount_of_money

        elif bet.bet_name == self.BetType.BASKET.value:
            if winning_number in bet.value:
                return self.coefficients[self.BetType.BASKET] * bet.amount_of_money
            else:
                return -bet.amount_of_money

        elif bet.bet_name == self.BetType.FIRST_FOUR.value:
            if winning_number in bet.value:
                return self.coefficients[self.BetType.FIRST_FOUR] * bet.amount_of_money
            else:
                return -bet.amount_of_money

        else:
            return -bet.amount_of_money
