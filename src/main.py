import os
from wordle_solver import WordleSolver
from wordle_game import WordleGame

answer = 'alarm'
path = os.path.join('../data', 'dict-wordle.txt')
cpath = os.path.join('../data', 'dict-common.txt')

word = WordleSolver(path, cpath, export_lexicon=False)

if answer:
    game = WordleGame(answer)
    word.reset()

    for i in range(6):
        guess_word = word.common[-1]
        result = game.guess(guess_word)

        if result == game.win_pattern:
            print(f'you won with {guess_word} in {game.guesses} tries!')
            break

        word.guess(guess_word, result)
