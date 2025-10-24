import typing
import random
from project.Task4.bet import Bet
from project.Task4.print_in_txt import print_in_txt

class Roulet:
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
        self.coefficients: typing.Dict[str, int] = {
            "straight": 35,
            "split": 17,
            "street": 11,
            "basket": 11,
            "first_four": 8,
            "corner": 8,
            "line": 5,
            "red_black": 1,
            "even_odd": 1,
            "dozen": 2,
            "column": 2,
            "less_more": 1,
        }

    def spin(self) -> int:
        """
        Spins the roulette wheel
        """
        return random.choice(self.numbers)

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
            print_in_txt(f"name: {key}, coefficients: {value}")

    def get_color(self, number: int) -> str:
        """
        Determines number color
        Takes: number
        Returns: color
        """
        if number == 0:
            return "green"
        elif number in self.red_numbers:
            return "red"
        else:
            return "black"

    def is_even(self, number: int) -> str:
        """
        Checks if number is even
        Takes: number
        Returns: 'even' or 'odd'.
        """
        if number % 2 == 0:
            return "even"
        else:
            return "odd"

    def get_less_more(self, number: int) -> str:
        """
        Determines number range
        Takes: number
        Returns: 'less' or 'more'
        """
        if number <= 18:
            return "less"
        else:
            return "more"

    def calculation_of_winning(self, bet: Bet, winning_number: int) -> int:
        """
        Calculates bet winnings
        Takes: bet, winning number
        Returns: amount
        """
        if bet.bet_name == "straight":
            if winning_number == bet.value:
                return self.coefficients["straight"] * bet.amount_of_money
            else:
                return -bet.amount_of_money

        elif bet.bet_name == "split":
            if winning_number in bet.value:
                return self.coefficients["split"] * bet.amount_of_money
            else:
                return -bet.amount_of_money

        elif bet.bet_name == "street":
            if (
                winning_number
                in self.numbers[(bet.value - 1) * 3 + 1 : bet.value * 3 + 1]
            ):
                return self.coefficients["street"] * bet.amount_of_money
            else:
                return -bet.amount_of_money

        elif bet.bet_name == "line":
            if (
                winning_number
                in self.numbers[(bet.value - 1) * 6 + 1 : bet.value * 6 + 1]
            ):
                return self.coefficients["line"] * bet.amount_of_money
            else:
                return -bet.amount_of_money

        elif bet.bet_name == "dozen":
            if (
                winning_number
                in self.numbers[(bet.value - 1) * 12 + 1 : bet.value * 12 + 1]
            ):
                return self.coefficients["dozen"] * bet.amount_of_money
            else:
                return -bet.amount_of_money

        elif bet.bet_name == "column":
            if winning_number in self.numbers[bet.value :: 3]:
                return self.coefficients["column"] * bet.amount_of_money
            else:
                return -bet.amount_of_money

        elif bet.bet_name == "corner":
            if winning_number in bet.value:
                return self.coefficients["corner"] * bet.amount_of_money
            else:
                return -bet.amount_of_money

        elif bet.bet_name == "red_black":
            if self.get_color(winning_number) == bet.value:
                return self.coefficients["red_black"] * bet.amount_of_money
            else:
                return -bet.amount_of_money

        elif bet.bet_name == "even_odd":
            if self.is_even(winning_number) == bet.value:
                return self.coefficients["even_odd"] * bet.amount_of_money
            else:
                return -bet.amount_of_money

        elif bet.bet_name == "less_more":
            if self.get_less_more(winning_number) == bet.value:
                return self.coefficients["less_more"] * bet.amount_of_money
            else:
                return -bet.amount_of_money

        elif bet.bet_name == "basket":
            if winning_number in bet.value:
                return self.coefficients["basket"] * bet.amount_of_money
            else:
                return -bet.amount_of_money

        else:
            if winning_number in bet.value:
                return self.coefficients["first_four"] * bet.amount_of_money
            else:
                return -bet.amount_of_money
