"""
Runs the actual 'loop' of the game
"""

import random  # randomly select word
from wordle import Wordle  # imports the Wordle class to generate
from termcolor import colored, cprint


def main():
	"""Runs main loop of the program and loads pre-reqs."""
	wordle_word_set = load_word_set('data/wordle_words.txt')
	allowed_words = load_word_set('data/english_words.txt')
	secret_word = choose_word(wordle_word_set)  # Selects secret word
	wordle_game = Wordle(secret_word)  # Creates the Wordle Game
	wordle_game.draw_board()  # Initializes the game board

	while wordle_game.can_play:
		usr_guess = input('What is your guess?: ').upper()

		if len(usr_guess) != wordle_game.WORD_LENGTH:
			cprint(f'Word must be {wordle_game.WORD_LENGTH}'
				   f' characters long!', 'red')
			continue

		if usr_guess not in allowed_words:
			cprint("Word does not exist!", 'red')
			continue

		result = wordle_game.guess(usr_guess)
		colored_guess = color_guess(result)
		wordle_game.update_board(colored_guess)
		wordle_game.draw_board()  # Draws the board to screen

	if wordle_game.wordle_solved:
		print('You solved the puzzle!')
	else:
		print('You failed to solve the puzzle...')
		print(f'The word was {secret_word}')


def color_guess(result):
	colored_guess = []
	for letter in result:
		if letter.is_in_position:
			c_letter = colored(letter.character, 'green')
		elif letter.is_in_word:
			c_letter = colored(letter.character, 'yellow')
		else:
			c_letter = colored(letter.character, 'light_red')
		colored_guess.append(c_letter)
	# test = " ".join(colored_guess)

	# print(test)
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
