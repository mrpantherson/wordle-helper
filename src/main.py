import os
import wordle

path = os.path.join('../data', 'dict-wordle.txt')
cpath = os.path.join('../data', 'dict-common.txt')
word = wordle.Wordle(path, cpath, export_lexicon=False)

word.term_frequency()
