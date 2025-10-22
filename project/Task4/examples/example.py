import random
from project.Task4.game import Game

number_of_rounds = random.choice(range(1, 101))
game = Game(number_of_rounds)
game.game_process()
