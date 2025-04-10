from string_package import *

if __name__ == "__main__":
    s = input("Sentence: ")
    np = remove_punctuation(s)
    print("Reversed:", reverse_string(s))
    print("Capitalized:", capitalize_words(s))
    print("Chars:", count_characters(np), "Words:", count_words(np), "Avg:", average_word_length(np))
