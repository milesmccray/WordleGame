"""
The back-end to make checks for the main loop in play_wordle.py
"""
from letterstate import LetterState
from termcolor import colored


class Wordle:
	MAX_ATTEMPTS = 6  # You can change this
	WORD_LENGTH = 5   # Changing this breaks the display board
	VOIDED_LETTER = '*'

	def __init__(self, secret_word):
		self.secret_word = secret_word.upper()
		self.guesses = []
		self.game_board = []
		self.answer = []
		self.usr_board = []

		# Creates the game board
		for i in range(self.MAX_ATTEMPTS):
			self.game_board.append('_' * self.WORD_LENGTH)

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
		"""Updates the game_board with colored usr_guess."""
		self.game_board[len(self.guesses)-1] = colored_guess
		self.draw_board()

	def draw_board(self):
		"""Draws the boarder and board to the screen."""
		# Board variables
		cborder = ['┏', '┓', '┗', '┛']
		hborder = '━'
		vborder = '┃'
		pad = ' '
		title = colored(' WORDLE', 'white', attrs=['bold'])

		# Draw the board
		print(cborder[0] + (hborder * 11) + cborder[1])
		print(vborder + (pad * 2) + title + (pad * 2) + vborder)
		# Unpacks the game_board list on every line
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
		"""Returns remaining attempts"""
		return self.MAX_ATTEMPTS - len(self.guesses)
