def reverse_string(s): return s[::-1]
def capitalize_words(s): return s.title()
def remove_punctuation(s):
    import string
    return s.translate(str.maketrans('', '', string.punctuation))
