def transpose(text):
    if not text:
        return ""

    rows = text.splitlines()
    width = max(len(r) for r in rows)
    result = []

    for c in range(width):
        out = []
        last_real = -1

        for r, row in enumerate(rows):
            if c < len(row):
                out.append(row[c])
                last_real = len(out) - 1
            else:
                out.append(" ")

        result.append("".join(out[: last_real + 1]))

    return "\n".join(result)