def abbreviate(text):
    text = text.replace("-", " ")
    text = text.replace("_", " ")

    for ch in ".,!?':;":
        text = text.replace(ch, "")

    result = ""
    for word in text.split():
        result += word[0].upper()

    return result