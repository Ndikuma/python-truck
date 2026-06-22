import re
from collections import Counter

def count_words(sentence):
    words = re.findall(r"[a-zA-Z0-9]+(?:'[a-zA-Z0-9]+)?", sentence.lower())
    return Counter(words)