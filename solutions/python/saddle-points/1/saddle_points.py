def saddle_points(matrix):
    if not matrix:
        return []

    row_len = len(matrix[0])

    # validate rectangular matrix
    for row in matrix:
        if len(row) != row_len:
            raise ValueError("irregular matrix")

    rows = len(matrix)
    cols = row_len

    # compute row max values
    row_max = [max(row) for row in matrix]

    # compute column min values
    col_min = []
    for c in range(cols):
        col_min.append(min(matrix[r][c] for r in range(rows)))

    result = []

    for r in range(rows):
        for c in range(cols):
            value = matrix[r][c]
            if value == row_max[r] and value == col_min[c]:
                result.append({"row": r + 1, "column": c + 1})

    return result