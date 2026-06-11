def annotate(garden):
    if garden is None:
        raise ValueError("The board is invalid with current input.")

    if not isinstance(garden, list):
        raise ValueError("The board is invalid with current input.")

    if len(garden) == 0:
        return []

    row_length = len(garden[0])

    # validate rectangular board + valid chars
    for row in garden:
        if len(row) != row_length:
            raise ValueError("The board is invalid with current input.")
        for ch in row:
            if ch not in (" ", "*"):
                raise ValueError("The board is invalid with current input.")

    rows = len(garden)
    cols = row_length

    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),         (0, 1),
        (1, -1),  (1, 0), (1, 1),
    ]

    def count_adjacent(r, c):
        count = 0
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                if garden[nr][nc] == "*":
                    count += 1
        return count

    result = []

    for r in range(rows):
        new_row = ""
        for c in range(cols):
            if garden[r][c] == "*":
                new_row += "*"
            else:
                n = count_adjacent(r, c)
                new_row += str(n) if n > 0 else " "
        result.append(new_row)

    return result