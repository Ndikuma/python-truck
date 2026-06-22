def proverb(*words, qualifier=None):
    if not words:
        return []

    result = []

    for i in range(len(words) - 1):
        result.append(f"For want of a {words[i]} the {words[i + 1]} was lost.")

    last_word = words[0]
    if qualifier:
        last_word = f"{qualifier} {last_word}"

    result.append(f"And all for the want of a {last_word}.")

    return result