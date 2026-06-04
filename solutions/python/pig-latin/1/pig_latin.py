import re

def translate_word(word):
    # Rule 1: Starts with a vowel sound (a, e, i, o, u, xr, yt)
    if re.match(r'^([aeiou]|xr|yt)', word):
        return word + "ay"
        
    # Rule 3: Consonants followed by "qu" (e.g., "square" -> "squ" + "are")
    match_qu = re.match(r'^([^aeiou]*qu)(.+)$', word)
    if match_qu:
        prefix, rest = match_qu.groups()
        return rest + prefix + "ay"
        
    # Rule 4: Consonants followed by "y" (e.g., "rhythm" -> "rh" + "ythm")
    match_y = re.match(r'^([^aeiou]+)(y.+)$', word)
    if match_y:
        prefix, rest = match_y.groups()
        return rest + prefix + "ay"
        
    # Rule 2: One or more consonants at the start (e.g., "chair" -> "ch" + "air")
    match_consonants = re.match(r'^([^aeiou]+)(.+)$', word)
    if match_consonants:
        prefix, rest = match_consonants.groups()
        return rest + prefix + "ay"

    return word


def translate(text):
    """Translate a sentence of one or more words into Pig Latin."""
    # Split the sentence into individual words, translate each, and glue them back together
    words = text.split()
    translated_words = [translate_word(word) for word in words]
    return " ".join(translated_words)