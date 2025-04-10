def count_characters(s): return len(s)
def count_words(s): return len(s.split())
def average_word_length(s):
    w = s.split()
    return sum(map(len, w)) / len(w) if w else 0
