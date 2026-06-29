class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if not isinstance(other, Point):
            return NotImplemented
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"


class WordSearch:
    def __init__(self, puzzle):
        self.puzzle = puzzle
        self.rows = len(puzzle)
        self.cols = len(puzzle[0]) if self.rows > 0 else 0

    def search(self, word):
        directions = [
            (0, 1),    # right
            (0, -1),   # left
            (1, 0),    # down
            (-1, 0),   # up
            (1, 1),    # down-right
            (1, -1),   # down-left
            (-1, 1),   # up-right
            (-1, -1)   # up-left
        ]

        for r in range(self.rows):
            for c in range(self.cols):
                if self.puzzle[r][c] != word[0]:
                    continue

                for dx, dy in directions:
                    if self._check_direction(word, r, c, dx, dy):
                        end_r = r + (len(word) - 1) * dx
                        end_c = c + (len(word) - 1) * dy
                        return (Point(c, r), Point(end_c, end_r))

        return None

    def _check_direction(self, word, r, c, dx, dy):
        for i, ch in enumerate(word):
            nr = r + i * dx
            nc = c + i * dy

            if not (0 <= nr < self.rows and 0 <= nc < self.cols):
                return False

            if self.puzzle[nr][nc] != ch:
                return False

        return True