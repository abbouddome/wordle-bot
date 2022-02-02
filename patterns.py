from collections import defaultdict
from enum import Enum

class Status(Enum):
    GREY = 0
    YELLOW = 1
    GREEN = 2

STR_TO_STATUS = {
    "absent": Status.GREY,
    "present": Status.YELLOW,
    "correct": Status.GREEN
}


class Pattern:
    def __init__(self, data, word, str_to_pattern=False):
        if str_to_pattern:
            self.pattern = self.generate_pattern_from_str(data, word)
        else:
            self.pattern = self.generate_pattern(data, word)

    def generate_pattern_from_str(self, str_status, guess):
        return [(STR_TO_STATUS[str], letter) for str, letter in zip(str_status, guess)]

    def generate_pattern(self):
        pass

    def readable_pattern(self):
        """Returns the string version of the pattern"""
        str_pattern = ""
        for data in self.pattern:
            str_pattern += str(data[0])
        return str_pattern


    
