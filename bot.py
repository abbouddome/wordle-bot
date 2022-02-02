
class WordleBot():
    def __init__(self):
        with open("dictionary.txt", "r") as file:
            self.remaining_words = file.read().split(" ")

    def calculate_optimal_word(self):
        pass