import os
import wordle

path = os.path.join('../data', 'dict-wordle.txt')
word = wordle.Wordle(path, export_lexicon=False)

word.term_frequency()
