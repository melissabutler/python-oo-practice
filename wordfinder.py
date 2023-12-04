"""Word Finder: finds random words from a dictionary."""

import random

class WordFinder:
    """Initiate class, connect to dictionary text file and turn into a parsable list"""
    def __init__(self, path):
        word_file = open(path, "r")

        data = word_file.read()

        self.words = data.split('\n')

        print(f"{len(self.words)} words read")

    def random(self):
        """Return a random word from the dictionary file."""
        return random.choice(self.words)
    
class SpecialWordFinder(WordFinder):

    def __init__(self, path):
        word_file = open(path, "r")

        data = word_file.read()

        self.words = data.split('\n')
    
    def parse(self):
        return [word.strip() for word in self.words
            if word.strip() and not word.startswith("#")]
        # for word in self.words:
        #     if word.startswith(" ") == True or word.startswith("#") == True:
        #         print(word)
        # # print(self.words)