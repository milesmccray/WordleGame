"""
Runs the actual 'loop' of the game
"""

from termcolor import colored, cprint  # Color implementation in console
import random  # randomly select word
from wordle import Wordle  # imports the Wordle class to generate
import os  # for clearing terminal


def main():
	"""Runs main loop of the program and loads pre-reqs."""
	word_set = load_word_set('data/wordle_words.txt')
	secret_word = choose_word(word_set)  # Selects secret word
	wordle_game = Wordle(secret_word)  # Creates the Wordle Game
	wordle_game.draw_board()  # Initializes the game board

	while wordle_game.can_play:
		print(secret_word)
		print(f'You have {wordle_game.remaining_attempts} attempts remaining')
		usr_guess = input('What is your guess?: ')
		lists = wordle_game.guess(usr_guess.upper())
		wordle_game.update_board(lists[0], lists[1])  # Updates game board
		wordle_game.draw_board()  # Draws the board to screen
		print('hi')

	if wordle_game.wordle_solved:
		print('You solved the puzzle!')
	else:
		print('You failed to solve the puzzle...')
		print(f'The word was {secret_word}')


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
