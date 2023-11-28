# Convert words from a "words.txt" and make it a wordle_words.txt

def main():
	input_file = 'words.txt'
	output_file = 'wordle_words.txt'
	five_letter_words = []

	# Opens input file and create a list of five-letter-words
	with open(input_file, 'r') as file:
		for line in file.readlines():
			word = line.strip()
			if len(word) == 5:
				five_letter_words.append(word)

	# Opens output file and writes to it
	with open(output_file, 'w') as file:
		for word in five_letter_words:
			file.write(word + '\n')

	print(f'Found {len(five_letter_words)}, five letter words')


if __name__ == '__main__':
	main()
