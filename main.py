import sys
from stats import (
    get_num_words,
    get_num_chars,
    sort_chars,
)
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        return sys.exit(1)
    book_path = sys.argv[1]
    num_words = get_num_words(book_path)
    num_chars = get_num_chars(book_path)
    sorted_chars = sort_chars(num_chars)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {str(num_words)} total words")
    print("--------- Character Count -------")
    for char in sorted_chars:
        if char["char"].isalpha():
            print(f"{char["char"]}: {char["amount"]}")
    print("============= END ===============")
main()
