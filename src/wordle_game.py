"""

"""


class WordleGame:

    """
    """

    win_pattern = 'ggggg'

    def __init__(self, secret_word):
        """
        """
        self.secret_word = secret_word
        self.guesses = 0

    def reset(self):
        self.guesses = 0

    def guess(self, guess):
        """"
        """
        results = []
        for g, c in zip(guess, self.secret_word):
            if g == c:
                results.append('g')
            elif g in self.secret_word:
                results.append('y')
            else:
                results.append('b')

        self.guesses += 1
        return ''.join(results)
