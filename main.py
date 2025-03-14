import sys
from stats import (
    get_word_count,
    get_character_count,
    get_sorted_characters
)


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    file_path = sys.argv[1]
    
    book_text = get_book_text(file_path)
    word_count = get_word_count(book_text)
    characters = get_character_count(book_text)
    sorted_characters = get_sorted_characters(characters)
    print_report(file_path, word_count, sorted_characters)



def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents


def print_report(book_path, num_words, chars_sorted_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char in chars_sorted_list:
        if char.isalpha():
            print(f"{char}: {chars_sorted_list[char]}")
    print("============= END ===============")


main()
