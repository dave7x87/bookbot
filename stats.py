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
        Then converts to a list
    """
    char_counts = count_chars(text)
    char_list = []
    for char in char_counts:
        char_list.append ({"char": char, "num": char_counts[char]})
    
    return char_list

def sort_on(dict):
    """ Return the list of keys to sort by"""

def sort_char_list(list):
    """  Takes the list of """
    