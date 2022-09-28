import time
from game import Game
from bot import WordleBot

def log_score(starting_guess, answer, turn_number):
    pass

def application(input_word=None):
    game = Game()
    bot = WordleBot()
    while game.running:
        try:
            if not input_word:
                word = bot.calculate_optimal_word() 
            else:
                word = input_word
                input_word = None
            turn_result = game.play_turn(word)
            if game.running:
                bot.turn_aftermath(turn_result)
        except KeyError:
            continue
    time.sleep(5)
