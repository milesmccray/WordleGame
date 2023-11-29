"""
GOALS:
BACK-END
- Gather 'all' 5-letter words and store in txt document. USE open()
GAME-PART
- Make sure the word exists using wordle_words and are 5 letters
- Tracking what letters are a part of the word
- Turn the game board lists into strings
- Change board from correct letters to the actual guess, color code the
letters
- Retry system, probably need to del class instance?
- DOuble check the usage of variables / list to make sure they are needed
VISUAL
- Create a simple terminal based interface
- Expand interface using tkinter?

The back-end to make checks for the main loop in play_wordle.py
"""

from letterstate import LetterState
from termcolor import colored


class Wordle:
	MAX_ATTEMPTS = 6
	WORD_LENGTH = 5
	VOIDED_LETTER = '*'

	def __init__(self, secret_word):
		self.secret_word = secret_word.upper()
		self.guesses = []
		self.empty_guess = ['_', '_', '_', '_', '_']
		self.empty_board = []
		self.game_board = []
		self.answer = []
		self.usr_board = []

		# Creates the game board
		for i in range(self.MAX_ATTEMPTS):
			self.game_board.append(self.empty_guess)

	def guess(self, word):
		"""Stores usr_guess in list & converts them into letter lists"""
		usr_guess = word
		self.guesses.append(usr_guess)
		secret_copy = list(self.secret_word)

		# Creates a LetterState object for each letter in guess
		result = [LetterState(x) for x in usr_guess]

		# Loops to see if letter is in correct position (GREEN)
		for i in range(self.WORD_LENGTH):
			letter = result[i]

			if letter.character == secret_copy[i]:
				letter.is_in_position = True
				secret_copy[i] = self.VOIDED_LETTER

		# Loops to see if letter is in the word (YELLOW)
		for i in range(self.WORD_LENGTH):
			letter = result[i]

			# Skips if letter already is in correct position
			if letter.is_in_position:
				continue

			# Checks every index in secret, for every one index in usr_guess
			for j in range(self.WORD_LENGTH):
				if letter.character == secret_copy[j]:
					letter.is_in_word = True
					secret_copy[j] = self.VOIDED_LETTER
					break

		# Returns a list of LetterState objects with flags set
		return result

	def update_board(self, colored_guess):
		self.game_board[len(self.guesses)-1] = colored_guess

	def draw_board(self):
		"""Draws the boarder and board to the screen."""
		cborder = ['┏', '┓', '┗', '┛']
		hborder = '━'
		vborder = '┃'
		pad = ' '
		print(cborder[0] + (hborder * 11) + cborder[1])
		print(vborder + pad*2 + ' WORDLE' + pad*2 + vborder)
		for i in self.game_board:
			print(vborder, *i, vborder)
		print(cborder[2] + (hborder * 11) + cborder[3])
		print(f'You have {self.remaining_attempts} attempts remaining')

	@property
	def wordle_solved(self):
		"""Returns True if the last guess is the secret word"""
		return len(self.guesses) > 0 and self.guesses[-1] == self.secret_word

	@property
	def can_play(self):
		"""Checks remaining attempts and if solved"""
		return self.remaining_attempts > 0 and not self.wordle_solved

	@property
	def remaining_attempts(self):
		return self.MAX_ATTEMPTS - len(self.guesses)
