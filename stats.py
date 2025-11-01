##stats.py

def get_num_words(text: str) -> int:
    """ Return the number of whitespace-separated words in text."""
    return len(text.split())

def count_chars(text: str) -> dict[str,int]:
    """ Return the counts of each unique character"""
    chars_seen = {}
    for char in text.lower():
        chars_seen[char] = chars_seen.get(char,0) + 1
    return chars_seen

def get_char_list(text: str) -> list[dict[str, int]]: 
    """ Takes the given text and produces a list of counts"""
    char_counts = count_chars(text)
    return [{"char": ch, "num": n} for ch, n in char_counts.items()]

def sort_on(items: dict[str, int]) -> int:
    """ A function that takes a dictionary and returns the value of the "num" key
        This is how the `.sort()` method knows how to sort the list of dictionaries
    """    
    return items["num"]

def get_sorted_chars(text: str) -> list[dict[str, int]]:
    """ Gets the character list and gets it sorted
        Returned as list of dictionaries
    """
    char_list = get_char_list(text)             # get list
    char_list.sort(reverse=True, key=sort_on)   # sort list
    return char_list