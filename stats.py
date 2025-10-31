def get_num_words(text):
    """Return the number of whitespace-separated words in text."""    
    return len(text.split())

def get_char_count(text):
    """ Return the counts of each unique character"""
    chars_seen = {}
    for char in str.lower(text):
        chars_seen[char] = chars_seen.get(char,0) + 1
    return chars_seen