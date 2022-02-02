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
        """Returns pattern by comparing turn result to guess"""
        return [(STR_TO_STATUS[str], letter) for str, letter in zip(str_status, guess)]

    def generate_pattern(self, word, guess):
        """Returns pattern by comparing a word to guess"""
        pattern = []
        greens = defaultdict(int)
        for a_letter, b_letter in zip(word, guess):
            if a_letter == b_letter:
                greens[b_letter] += 1

        occurences = defaultdict(int)
        for a_letter, b_letter in zip(word, guess):
            if a_letter == b_letter:
                pattern.append((TILE.GREEN, b_letter))
            else:
                tile = TILE.YELLOW if b_letter in word and occurences[b_letter] < word.count(b_letter) - greens[b_letter] else TILE.GREY
                pattern.append((tile, b_letter))
                occurences[b_letter] += 1
        
        return pattern 

    def readable_pattern(self):
        """Returns the string version of the pattern"""
        str_pattern = ""
        for tile, _ in self.pattern:
            if tile == TILE.GREY:
                str_pattern += "0"
            if tile == TILE.YELLOW:
                str_pattern += "1"
            if tile == TILE.GREEN:
                str_pattern += "2"
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
        


    
