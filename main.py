import sys
if len(sys.argv) != 2:
	print("Usage: python3 main.py <path_to_book>")
	sys.exit(1)
path_to_file = sys.argv[1]

def get_book_text(path_to_file):
	with open(path_to_file) as f:
		file_contents = f.read()
	return file_contents

word_count = 0

from stats import count_words
from stats import count_characters
from stats import list_characters

def main():
	file = get_book_text(path_to_file)
	word_count = count_words(file)
	character_count = count_characters(file)
	print("============ BOOKBOT ============")
	print(f"Analyzing book found at {path_to_file}...")
	print("----------- Word Count ----------")
	print(f"Found {word_count} total words")
	print("--------- Character Count -------")
	for character in list_characters(character_count):
		print(f"{character['char']}: {character['num']}")
	print("============= END ===============")
	
main()

