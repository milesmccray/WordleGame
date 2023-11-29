"""
Runs the actual 'loop' of the game
"""

import random
from wordle import Wordle
from termcolor import colored, cprint

def main():
	"""Runs main loop of the program and loads pre-reqs."""
	# Loads word sets needed to run the game
	wordle_word_set = load_word_set('data/wordle_words.txt')
	allowed_words = load_word_set('data/english_words.txt')

	# Chooses secret_word and creates the wordle object + display board
	secret_word = choose_word(wordle_word_set)
	wordle_game = Wordle(secret_word)
	wordle_game.draw_board()

	# Main loop of the game
	while wordle_game.can_play:
		usr_guess = input('What is your guess?: ').upper()

		# Checks if usr_guess is equal to the WORD_LENGTH var.
		if len(usr_guess) != wordle_game.WORD_LENGTH:
			cprint(f'Word must be {wordle_game.WORD_LENGTH}'
				   f' characters long!', 'light_red')
			continue

		# Checks if usr_guess is a real word against the data set
		if usr_guess not in allowed_words:
			cprint("Word does not exist!", 'light_red')
			continue

		result = wordle_game.guess(usr_guess)
		colored_guess = color_guess(result)
		wordle_game.update_board(colored_guess)

	if wordle_game.wordle_solved:
		print('You solved the puzzle!')
	else:
		print('You failed to solve the puzzle...')
		print(f'The word was {secret_word}')


def color_guess(result):
	colored_guess = []
	for letter in result:
		if letter.is_in_position:
			c_letter = colored(letter.character, 'light_green')
		elif letter.is_in_word:
			c_letter = colored(letter.character, 'light_yellow')
		else:
			c_letter = colored(letter.character, 'light_red')
		colored_guess.append(c_letter)

	return colored_guess


def load_word_set(path):
	"""Converts loaded word_set into a set() and returns."""
	with open(path, 'r') as file:
		word_set = set((line.rstrip() for line in file))
	return word_set


def choose_word(word_set):
	"""Randomly selects a word from the set word_set and returns."""
	secret_word = random.choice(list(word_set))
	return secret_word.upper()


if __name__ == '__main__':
	main()
