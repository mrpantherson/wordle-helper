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
    correct : array[str]
        keep track of correctly guessed letters so we don't accidentally remove them
    common : array[str]
        list of common words from Google's n-gram frequency analysis

    Methods
    -----------------
    doesnt_have(letter=None)
        removes words that have the letter passed in
    has(letter=None)
        removes words that do not have the letter passed in
    has_at(letter=None, at=None)
        removes words that do not have the letter at the specified index
    whats_left()
        print the remaining words (full or common only)
    check_letter_at(letter=None, at=None)
        similar to has_at, but only prints the words that have a letter at the specified index
    term_frequency()
        calculates the term frequency to suggest words to use for guessing
    """

    def __init__(self):
        print('call load_lexicon or consider using another constructor')

    def __init__(self, path, cpath, export_lexicon=False, word_len=5):
        self.load_lexicon(path, cpath, export_lexicon, word_len)

    def load_lexicon(self, path, common_path, export_lexicon=False, word_len=5):
        """
        Arguments
        --------------
        path : dir/filename of dictionary to be used
        export_lexicon : flag to see if worldle should export trimmed dictionary
        word_len : how long the words are in the puzzle
        """
        self.word_len = word_len
        self.correct = []
        
        with open(path) as f:
            self.original = f.read() 
            self.original = [x for x in self.original.split('\n') if len(x) == self.word_len]
            self.lexicon = self.original.copy()

        with open(common_path) as f:
            self.common = f.read() 
            self.common = [x for x in self.common.split('\n') if len(x) == self.word_len]
            self.common_original = self.common.copy()

        if export_lexicon:
            with open(path, 'w') as f:
                for word in self.lexicon:
                    f.write(f'{word}\n')
        
        print(f'Wordle has {len(self.original)} words available.')

    def reset(self):
        """
        If you are playing a new puzzle (or messed up the clues) use this to rest dict
        """
        self.lexicon = self.original.copy()
        self.common = self.common_original.copy()
        self.correct = []

    def doesnt_have(self, letters=None):
        """
        Arguments
        ---------------
        letters : a string, or array of strings to filter lexicon by
        """

        try:
            n_letters = len(letters)
        except TypeError:
            letter = list(letters)

        for l in letters:
            # bit of a hack, but if you guess a letter multiple times this remove function
            # could elimate valid words, would be best to keep track of position/value of
            # correct guesses and compare that to items being removed
            if l in self.correct:
                print(f'{l} already guessed, skipping')
                continue

            n_words = len(self.lexicon)
            self.lexicon = [x for x in self.lexicon if not l in x]
            self.common = [x for x in self.common if not l in x]
            print(f'{l} - removed {n_words - len(self.lexicon):<5} {len(self.lexicon)} remaining.')

    def has(self, letter=None, *, at=None, not_at=None):
        """
        Arguments
        ---------------
        letter : string, character the word has
        at : int, which position the letter is (green)
        not_at : int, which position the letter is not at (yellow)
        """

        n_words = len(self.lexicon)

        if not_at is not None:
            self.lexicon = [x for x in self.lexicon if letter in x and x[not_at] != letter]
            self.common = [x for x in self.common if letter in x and x[not_at] != letter]
        else:
            self.lexicon = [x for x in self.lexicon if x[at] == letter]
            self.common = [x for x in self.common if x[at] == letter]
            self.correct.append(letter)

        print(f'{letter} - removed {n_words - len(self.lexicon):<5} {len(self.lexicon)} remaining.')

    def whats_left(self, common_only=True):
        """
        Print all possible remaining words, or just the common ones
        """
        if common_only:
            print(self.common)
        else:
            print(self.lexicon)

    def term_frequency(self):
        """
        This function gets the current lexicon's term frequency and then displays the most
        'valuable' words based on non-repeating high tf. This helps elimates words from
        the lexicon e.g. if you guess 'fuzzy' and wordle tells you the 'z' is nowhere in
        the word, that isn't very helpful, however if a letter with a high tf is nowhere
        in the word then you can elimate a large number of possibilites.
        """
        
        term_count = len(self.lexicon) * self.word_len
        # count each term and convert it to a tf
        freq = Counter()
        for word in self.lexicon:
            freq.update(word)
        freq = {k: v/term_count for k,v in freq.items()}

        # calculate how "valuable" each word is in terms of the frequency of letters it contains
        # this should help us narrow down letters e.g. 'arose' has more common letters than 'kudzu'
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

    def guess(self, word, results):
        """
        Automate inputs, just put in what you guessed along with the results from the puzzle
        E.g. word.guess('slimy', 'bbygg')
        
        Arguments
        ---------------
        word : what word was guessed
        
        results : the color results for each letter (b=black, g=green, y=yellow)
        """

        for i, (letter, color) in enumerate(zip(word, results)):
            if color == 'b':
                self.doesnt_have(letter)
            elif color == 'g':
                self.has(letter, at=i)
            elif color == 'y':
                self.has(letter, not_at=i)
            else:
                print('Invalid result passed')

        print('\nTry one of the following to narrow down choices]')
        self.term_frequency()

