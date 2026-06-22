def decode(text):
    result = []
    count = ""

    for ch in text:
        if ch.isdigit():
            count += ch
        else:
            n = int(count) if count else 1
            result.append(ch * n)
            count = ""

    return "".join(result)
    
def encode(text):
    if not text:
        return ""

    result = []
    count = 1

    for i in range(1, len(text)):
        if text[i] == text[i - 1]:
            count += 1
        else:
            if count > 1:
                result.append(str(count))
            result.append(text[i - 1])
            count = 1

    # last group
    if count > 1:
        result.append(str(count))
    result.append(text[-1])

    return "".join(result)