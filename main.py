def get_book_text(file_path):
    """ Read and return the book text from a file path."""
    with open(file_path) as file:
        return file.read()

from stats import get_num_words, get_sorted_chars #get_char_count

def main():
    
    book_path = "books/frankenstein.txt"
    
    text = get_book_text(book_path)
    
    num_words = get_num_words(text)
    print(f"Found {num_words} total words")
    
    """ Disable code pending refactoring for expanded/new functionality
    
    char_counts = get_char_count(text)
    print("Character counts:")
    for char in sorted(char_counts.keys()):
        print(f"{char!r}: {char_counts[char]}")
    
    """

    ##TEST CODE ONLY
    char_counts = get_sorted_chars(text)
    print(char_counts)


main()