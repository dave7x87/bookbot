def get_book_text(file_path):
    """ Read and return the book text from a file path."""
    with open(file_path) as file:
        return file.read()

from stats import get_num_words, get_sorted_chars #get_char_count

def main():
    
    book_path = "books/frankenstein.txt"    # Set book to read in
    
    text = get_book_text(book_path)         # Read book
    
    # Get report values
    num_words = get_num_words(text)         # word counts
    char_counts = get_sorted_chars(text)    # character counts

    # Begin report generation
    # Header first
    print ("============ BOOKBOT ============")
    print (f"Analyzing book found at {book_path}")
    # Add word count
    print ("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    # Add character count
    print ("--------- Character Count -------")
    # filter out non alphabet characters
    for char in char_counts:
        if char["char"].isalpha():
            print(f"{char["char"]}: {char["num"]}")
    # and then just add the footer
    print ("============= END ===============")

main()