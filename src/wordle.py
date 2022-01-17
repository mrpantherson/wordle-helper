from collections import Counter

""" This is a tool to help solve Wordle puzzles
"""

class Wordle:

    """
    A simple wordle helper

    Attributes
    -----------------
    original : array[str]
        lexicon to use for checking wordle matches
    lexicon : array[str]
        words that the object is considering, functions remove from this
    word_len : int
        length of words in the puzzle

    Methods
    -----------------
    doesnt_have(letter=None)
        removes words that have the letter passed in
    has(letter=None)
        removes words that do not have the letter passed in
    has_at(letter=None, at=None)
        removes words that do not have the letter at the specified index
    whats_left()
        print the remaining words
    check_letter_at(letter=None, at=None)
        similar to has_at, but only prints the words that have a letter at the specified index
    term_frequency()
        calculates the term frequency to suggest words to use for guessing
    """

    def __init__(self, path):
        self.word_len = 5
        self.original = open(path).read() 
        self.original = [x for x in self.original.split('\n') if len(x) == self.word_len]
        self.lexicon = self.original.copy()

        print(f'Wordle has {len(self.original)} words available.')

    def doesnt_have(self, letter=None):
        n_words = len(self.lexicon)
        self.lexicon = [x for x in self.lexicon if not letter in x]
        print(f'{letter} has removed {n_words - len(self.lexicon)} words.')

    def has(self, letter=None):
        n_words = len(self.lexicon)
        self.lexicon = [x for x in self.lexicon if letter in x]
        print(f'{letter} has removed {n_words - len(self.lexicon)} words.')

    def has_at(self, letter=None, at=None):
        n_words = len(self.lexicon)
        self.lexicon = [x for x in self.lexicon if x[at] == letter]
        print(f'{letter} has removed {n_words - len(self.lexicon)} words.')

    def whats_left(self):
        print(self.lexicon)

    def check_letter_at(self, letter=None, at=None):
        output = [x for x in self.lexicon if x[at] == letter]
        print(output)

    def term_frequency(self):
        term_count = len(self.lexicon) * self.word_len
        freq = Counter()
        for word in self.lexicon:
            freq.update(word)

        self.freq = {x:0 for x in self.lexicon}
        for key in self.freq.keys():
            value = 0
            # set is an easy way to remove duplicates, if we don't remove these then words with
            # repeating high value letters will seem more valuable e.g. reese
            for letter in ''.join(set(key)):
                value += freq[letter]
            self.freq[key] = value

        self.freq = sorted(self.freq, key=self.freq.get)
        print(self.freq[-5:])





