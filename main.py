## main.py
#Imports
from stats import get_num_words, get_sorted_chars

#Set report constants
HEADER = "============ BOOKBOT ============"
FOOTER = "============= END ==============="

def get_book_text(file_path: str) -> str:
    """ Read and return the book text from a file path."""
    with open(file_path) as file:
        return file.read()
    
def print_report(book_path: str, word_count: int, char_counts: list[dict[str, int]]) -> None: 
    """ Prints report"""
    print(HEADER)
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")  
    for entry in char_counts:
        if entry["char"].isalpha():
            print(f"{entry['char']}: {entry['num']}")
    print(FOOTER)

def main() -> None:

    book_path = "books/frankenstein.txt"    # Set book to read in
    text = get_book_text(book_path)         # Read book
    # Get report values
    num_words = get_num_words(text)         # word counts
    char_counts = get_sorted_chars(text)    # character counts
    print_report(book_path, num_words, char_counts)

if __name__ == "__main__":                  #import guard
    main()