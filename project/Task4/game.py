from project.Task4.roulet import Roulet
from project.Task4.move import Move
from project.Task4.bet import Bet
from project.Task4.player import Player
import typing
from project.Task4.print_in_txt import print_in_txt


class Game:
    def __init__(self, number_of_rounds: int, player: typing.List[Player]) -> None:
        """
        Creates a game
        Takes: number of rounds
        """
        self.number_of_rounds = number_of_rounds
        self.player = player

    def game_process(self) -> None:
        """
        Starts and manages the game process
        """
        print_in_txt(
            "Welcome to my implementation of the roulette game (only bots play)"
        )
        roulet = Roulet()
        roulet.displaying_name_of_bets()
        roulet.get_black_number()
        roulet.get_red_number()

        player_str = "Players: "
        for i, bot in enumerate(self.player):
            if i > 0:
                player_str += ", "
            player_str += f"{bot.name} - {bot.balance}"
        player_str += "\n"
        print_in_txt(player_str)

        for bot in self.player:
            bot.current_bet = bot.make_bet()

        print_in_txt("The game begins")

        first = input("press Enter to start the first round...")
        for i in range(self.number_of_rounds):
            active_bots = [
                bot for bot in self.player if not bot.is_bankrupt() and bot.current_bet
            ]
            if len(active_bots) == 0:
                break

            for bot in active_bots:
                bot.current_bet = bot.make_bet()

            winning_number = roulet.spin()

            move = Move(self.player, roulet)
            move.round(winning_number)

            move.displaying_information(winning_number)

            bankrupt = []
            for bot in self.player:
                if bot.is_bankrupt() or (
                    bot.current_bet and bot.current_bet.amount_of_money == 0
                ):
                    bankrupt.append(bot)

            for bot in bankrupt:
                print_in_txt(f"{bot.name} has gone bankrupt and is leaving the game!")
                bot.current_bet = None

            self.player = [bot for bot in self.player if bot not in bankrupt]

            enter = input(f"Press Enter to start the {i+1} round...")

        print_in_txt("This round will not be held. Our game is over")
