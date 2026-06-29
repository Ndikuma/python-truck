def rows(row_count):
    if row_count < 0:
        raise ValueError("number of rows is negative")

    if row_count == 0:
        return []

    if row_count == 1:
        return [[1]]

    triangle = rows(row_count - 1)
    prev = triangle[-1]

    row = [1]
    for i in range(len(prev) - 1):
        row.append(prev[i] + prev[i + 1])
    row.append(1)

    triangle.append(row)
    return triangle