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
VISUAL
- Create a simple terminal based interface
- Expand interface using tkinter?

The back-end to make checks for the main loop in play_wordle.py
"""


class Wordle:
	MAX_ATTEMPTS = 6
	WORD_LENGTH = 5

	def __init__(self, secret_word):
		self.secret_word = secret_word.upper()
		self.guesses = []
		self.empty_board = ['_', '_', '_', '_', '_']
		self.temp_board = ['_', '_', '_', '_', '_']
		self.game_board = []

		# Creates the game board
		for i in range(self.MAX_ATTEMPTS):
			self.game_board.append(self.empty_board)

	def guess(self, word):
		"""Stores usr_guess in list & converts them into letter lists"""
		usr_guess = word
		self.guesses.append(usr_guess)

		# Turns both the secret_word and usr_guess to a list and return
		x = list(usr_guess)
		y = list(self.secret_word)
		lists = [x, y]
		return lists

	def update_board(self, usr_list, secret_list):
		"""Updates game_board variable depending on overlapping letters."""

		# Compares the usr/secret letter lists for matches
		for index, (x, y) in enumerate(zip(usr_list, secret_list)):
			if x == y:
				self.temp_board[index] = x  # Overwrites letter loc. on temp
			# Assigns the game_board index list to the temp_board
			self.game_board[(len(self.guesses) - 1)] = self.temp_board
		# Resets the TEMP board for next attempt
		self.temp_board = ['_', '_', '_', '_', '_']

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
