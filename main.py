from stats import get_book_text
from stats import get_word_count
from stats import get_char_count
from stats import dictionary_to_sorted_list
import sys

def main():

    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path_to_file = sys.argv[1]
#    path_to_file = "books/frankenstein.txt"
    contents = get_book_text(path_to_file)
    word_count = get_word_count(contents)
    letters = get_char_count(contents)
#    print(letters)
    sorted_list = dictionary_to_sorted_list(letters)
#    print(sorted_list)
#    print(contents)
#    print(f"{word_count} words found in the document")
#    print(letters)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_file}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for entry in sorted_list:
        if entry["char"].isalpha():
            print(f"{entry["char"]}: {entry["num"]}")
    print("============= END ===============")

main()