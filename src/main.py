import os
import wordle

# TODO qol stuff, maybe color code functions? combine has and has at?
# TODO there is a bug here where if a letter has already been guessed, but that letter is
# gussed again in another wrong spot, if you try to remove it, it will remove a valid word,
# maybe keep a list of 'has' words and don't remove them? otherwise we might have to keep track
# of 'doesnt_have' positions which would be annoying

path = os.path.join('../data', 'dict.txt')
word = wordle.Wordle(path)