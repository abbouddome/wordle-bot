from game import Game
from bot import WordleBot

if "__name__" == "__main__":
    game = Game()
    bot = WordleBot()
    while game.running:
        word = bot.calculate_optimal_word()
        game.play_turn(word)