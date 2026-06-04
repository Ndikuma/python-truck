import string

def is_pangram(sentence):
    # 1. Convert the entire sentence to lowercase
    lower_sentence = sentence.lower()
    
    # 2. Track all 26 lowercase letters ('abcdefghijklmnopqrstuvwxyz')
    alphabet = set(string.ascii_lowercase)
    
    # 3. Check if the alphabet set is a subset of the characters in the sentence
    return alphabet.issubset(set(lower_sentence))