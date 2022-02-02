from collections import defaultdict
from enum import Enum

class TILE(Enum):
    GREY = 0
    YELLOW = 1
    GREEN = 2

STR_TO_STATUS = {
    "absent": TILE.GREY,
    "present": TILE.YELLOW,
    "correct": TILE.GREEN
}


class Pattern:
    def __init__(self, data, word, turn_to_pattern=False):
        if turn_to_pattern:
            self.pattern = self.generate_pattern_from_turn(data, word)
        else:
            self.pattern = self.generate_pattern(data, word)

    def generate_pattern_from_turn(self, str_status, guess):

        return [(STR_TO_STATUS[str], letter) for str, letter in zip(str_status, guess)]

    def generate_pattern(self):
        pass

    def readable_pattern(self):
        """Returns the string version of the pattern"""
        str_pattern = ""
        for data in self.pattern:
            str_pattern += str(data[0])
        return str_pattern

    @staticmethod
    def count_occurences(guess):
        """Returns dict that says the occurences of letters"""
        occurences = defaultdict(int)
        for letter in guess:
            occurences[letter] += 1
        return occurences

    @staticmethod
    def count_tile_occurences(pattern):
        """Returns dict that says the occurences of green and yellow tiles"""
        occurences = defaultdict(int)
        for tile, letter in pattern:
            if tile == TILE.GREEN or tile == TILE.YELLOW:
                occurences[letter] += 1
        return occurences
        


    
