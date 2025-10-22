from project.Task4.roulet import Roulet
from project.Task4.bots import External_bids_only_bot, Straight_only_bot, Random_bot
from project.Task4.move import Move
from project.Task4.bet import Bet
from project.Task4.player import Player
import typing


class Game:
    def __init__(self, number_of_rounds: int) -> None:
        """
        Creates a game
        Takes: number of rounds
        """
        self.number_of_rounds = number_of_rounds

    def game_process(self) -> None:
        """
        Starts and manages the game process
        """
        print("Welcome to my implementation of the roulette game (only bots play)")
        roulet = Roulet()
        roulet.displaying_name_of_bets()
        print()
        roulet.get_black_number()
        roulet.get_red_number()
        print()

        balance = 1000

        ext_bot = External_bids_only_bot(balance)
        straight_bot = Straight_only_bot(balance)
        random_bot = Random_bot(balance)
        print(
            f"Players: {ext_bot.name} - {ext_bot.balance}, {straight_bot.name} - {straight_bot.balance}, {random_bot.name} - {random_bot.balance}\n"
        )

        bets: typing.Dict[Player, Bet] = {
            ext_bot: ext_bot.make_bet(),
            straight_bot: straight_bot.make_bet(),
            random_bot: random_bot.make_bet(),
        }
        print("The game begins\n")

        first = input("press Enter to start the first round...")
        for i in range(self.number_of_rounds):
            if len(bets) == 0:
                break
            for bot in bets.keys():
                bets[bot] = bot.make_bet()

            winning_number = roulet.spin()

            move = Move(bets, roulet)
            move.round(winning_number)

            print()
            move.displaying_information(winning_number)

            bankrupt = []
            for bot in bets.keys():
                if bot.is_bankrupt():
                    bankrupt.append(bot)
                if bets[bot].amount_of_money == 0:
                    bankrupt.append(bot)
                else:
                    continue
            for bot in bankrupt:
                del bets[bot]

            enter = input(f"Press Enter to start the {i+1} round...")

        print("This round will not be held. Our game is over")
