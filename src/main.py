import os
import wordle
import wordle_game as game


path = os.path.join('../data', 'dict-wordle.txt')
cpath = os.path.join('../data', 'dict-common.txt')

word = wordle.Wordle(path, cpath, export_lexicon=False)
game = game.WordleGame('sharp')

for i in range(6):
    guess_word = word.freq[-1]
    result = game.guess(guess_word)

    if result == 'ggggg':
        print(f'you won with {guess_word} in {game.guesses} tries!')
        break

    word.guess(guess_word, result)
