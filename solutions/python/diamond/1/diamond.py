def rows(letter: str):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    n = alphabet.index(letter)

    size = 2 * n + 1
    result = []

    for i in range(n + 1):
        char = alphabet[i]
        outer_spaces = n - i

        if i == 0:
            row = " " * outer_spaces + "A" + " " * outer_spaces
        else:
            inner_spaces = 2 * i - 1
            row = (
                " " * outer_spaces +
                char +
                " " * inner_spaces +
                char +
                " " * outer_spaces
            )

        result.append(row)

    bottom = result[:-1][::-1]
    return result + bottom