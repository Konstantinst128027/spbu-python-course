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

        bet = random.choice(list(self.BetType)).value

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
        bet_value = random.randint(0,36)

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

        bet = random.choice(list(self.BetType)).value

        match bet:
            case "red_black":
                bet_value = random.choice(["red", "black"])
    
            case "even_odd":
                bet_value = random.choice(["even", "odd"])
    
            case "less_more":
                bet_value = random.choice(["less", "more"])
    
            case "straight":
                bet_value = random.randint(0,36)
    
            case "split":
                first = random.randint(4, 33)
                match first % 3:
                    case 0:
                        second = random.choice([first - 1, first + 3, first - 3])
                    case 1:
                        second = random.choice([first + 1, first + 3, first - 3])
                    case 2:
                        second = random.choice([first + 1, first + 3, first - 3, first - 1])
                bet_value = [first, second]
    
            case "street":
                bet_value = random.randint(1, 13)
    
            case "basket":
                bet_value = random.choice([[0, 1, 2], [0, 2, 3]])
    
            case "first_four":
                bet_value = [0, 1, 2, 3]
    
            case "corner":
                first = random.randint(1, 37)
                match first:
                    case 1:
                        bet_value = [1, 2, 3, 4]
                    case 2:
                        bet_value = random.choice([[2, 3, 5, 6], [1, 2, 4, 5]])
                    case 3:
                        bet_value = [2, 3, 5, 6]
                    case 34:
                        bet_value = [31, 32, 34, 35]
                    case 35:
                        bet_value = random.choice([[31, 32, 34, 35], [32, 33, 35, 36]])
                    case 36:
                        bet_value = [32, 33, 35, 36]
                    case _:
                        match first % 3:
                            case 1:
                                second = random.choice([-3, 3])
                                bet_value = [first, first + 1, first + second, first + 1 + second]
                            case 0:
                                second = random.choice([-3, 3])
                                bet_value = [first, first - 1, first + second, first - 1 + second]
                            case 2:
                                second = random.choice([-3, 3])
                                third = random.choice([-1, 1])
                                bet_value = [first, first + third, first + second, first + third + second]
    
            case "line":
                bet_value = random.randint(1, 7)
    
            case "column":
                bet_value = random.randint(1, 4)
    
            case "dozen":
                bet_value = random.randint(1, 4)

        bet_amount = self.balance // random.randint(1, 10)
        self.bets.append((bet, bet_value, bet_amount))

        return Bet(bet, bet_value, bet_amount)
