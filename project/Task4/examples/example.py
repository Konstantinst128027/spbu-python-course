import random
from project.Task4.game import Game
from project.Task4.bots import External_bids_only_bot, Straight_only_bot, Random_bot

number_of_rounds = 20
bots = [
    External_bids_only_bot(1000),
    Straight_only_bot(1000),
    Random_bot(1000)
]
game = Game(number_of_rounds, bots)
game.game_process()
