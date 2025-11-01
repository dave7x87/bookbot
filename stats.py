def get_num_words(text):
    """ Return the number of whitespace-separated words in text."""
    
    return len(text.split())

def count_chars(text):
    """ Return the counts of each unique character
        Counts returned as dictionary
    """
    
    chars_seen = {}

    for char in str.lower(text):
        chars_seen[char] = chars_seen.get(char,0) + 1

    return chars_seen

def get_char_list(text):
    """ Takes the given text, passes to count_chars for counting
        Then converts to a list of dictionaries
    """
    
    char_counts = count_chars(text)
    char_list = []
    for char in char_counts:
        count = char_counts[char]
        char_list.append ({"char": char, "num": count})
    
    return char_list

def sort_on(list):
    """ A function that takes a dictionary and returns the value of the "num" key
        This is how the `.sort()` method knows how to sort the list of dictionaries
    """
    
    return list["num"]

def get_sorted_chars(text):
    """ Gets the character list and gets it sorted
        Returned as list of dictionaries
    """

    char_list = get_char_list(text)                 # get list
    char_list.sort(reverse=True, key=sort_on)   # sort list

    return char_list