import time
from game import Game
from bot import WordleBot

def application():
    game = Game()
    bot = WordleBot()
    automatic = True
    input_word = "pedro"
    while game.running:
        try:
            if automatic:
                word = bot.calculate_optimal_word() 
            else:
                word = input_word
                automatic = True
            turn_result = game.play_turn(word)
            if game.running:
                bot.turn_aftermath(turn_result)
        except KeyError:
            continue
    time.sleep(5)
