from game import Game
from bot import WordleBot

if __name__ == "__main__":
    game = Game()
    bot = WordleBot()
    while game.running:
        word = bot.calculate_optimal_word()
        turn_result = game.play_turn(word)
        if game.running:
            bot.turn_aftermath(turn_result)

