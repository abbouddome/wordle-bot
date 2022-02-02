from collections import defaultdict
import math
import random
from patterns import TILE, Pattern

FILE_NAME = "dictionary.txt"

class WordleBot():
    def __init__(self):
        self.dictionary = DictionaryReader()

    def calculate_optimal_word(self):
        """Calculates the optimal word"""
        if len(self.dictionary.valid_words) != self.dictionary.num_of_words:
            info_gains = self.generate_all_weights()
            optimal_word = info_gains[0][1]
        else:
            #optimal_word = random.choice(self.dictionary.words_remianing)
            optimal_word = "soare"
        return optimal_word

    def turn_aftermath(self, turn):
        self.dictionary.words_remianing = self.update_dictionaries(turn, self.dictionary.words_remianing)
        self.dictionary.valid_words = self.update_dictionaries(turn, self.dictionary.valid_words)

    def update_dictionaries(self, turn, word_dict):
        """Returns dictionary with filtered out words dependant on turn outcome"""
        word_dict = self.dictionary.words_remianing
        letter_occur = Pattern.count_occurences(turn.guess)
        green_yellow_occur = Pattern.count_tile_occurences(turn.pattern.pattern)
        for i, (tile, letter) in enumerate(turn.pattern.pattern):
            if tile == TILE.GREEN:
                word_dict = [word for word in word_dict if word[i] == letter]
            elif tile == TILE.YELLOW:
                word_dict = [word for word in word_dict if word[i] != letter and word.count(letter) >= green_yellow_occur[letter]]
            elif tile == TILE.GREY:
                word_dict = [word for word in word_dict if word[i] != letter and word.count(letter) < letter_occur[letter]]
        return word_dict

    def generate_weight_by_entropy(self, word):
        """Returns the entropy of word after comparing pattern of word and all other valid words"""
        num_of_words = len(self.dictionary.words_remianing)
        pattern_dict = defaultdict(int)
        for remain_word in self.dictionary.words_remianing:
            pattern = Pattern(remain_word, word).readable_pattern()
            pattern_dict[pattern] += 1 / num_of_words

        info_gain = -1 * sum([val * math.log(val) for val in pattern_dict.values()])
        return info_gain

    def generate_all_weights(self):
        """Returns list of tuples of words and weights in descending order"""
        info_gains = [(self.generate_weight_by_entropy(word), word) for word in self.dictionary.valid_words]
        return list(reversed(sorted((info_gains))))

class DictionaryReader:
    def __init__(self):
        file_contents = self.read_file()
        self.words_remianing = file_contents[0]
        self.valid_words = file_contents[1] + self.words_remianing
        self.num_of_words = len(self.valid_words)
    
    def read_file(self):
        """Reads file, returns result as a list of lines"""
        with open(FILE_NAME, "r") as file:
            lines = []
            for line in file.readlines():
                lines.append(line.split(" "))
        return lines