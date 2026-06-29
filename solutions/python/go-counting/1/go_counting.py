WHITE = 'W'
BLACK = 'B'
NONE = ''


class Board:
    def __init__(self, board):
        self.board = board
        self.h = len(board)
        self.w = len(board[0]) if board else 0

    def _valid(self, x, y):
        return 0 <= x < self.w and 0 <= y < self.h

    def _neighbors(self, x, y):
        result = []
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if self._valid(nx, ny):
                result.append((nx, ny))
        return result

    def territory(self, x, y):
        if not self._valid(x, y):
            raise ValueError('Invalid coordinate')
        
        if self.board[y][x] != ' ':
            return NONE, set()
        
        visited = set()
        queue = [(x, y)]
        territory = set()
        borders = set()
        
        while queue:
            cx, cy = queue.pop()
            if (cx, cy) in visited:
                continue
            visited.add((cx, cy))
            territory.add((cx, cy))
            
            for nx, ny in self._neighbors(cx, cy):
                cell = self.board[ny][nx]
                if cell == ' ' and (nx, ny) not in visited:
                    queue.append((nx, ny))
                elif cell in (BLACK, WHITE):
                    borders.add(cell)
        
        owner = borders.pop() if len(borders) == 1 else NONE
        return owner, territory

    def territories(self):
        result = {BLACK: set(), WHITE: set(), NONE: set()}
        visited = set()
        
        for y in range(self.h):
            for x in range(self.w):
                if self.board[y][x] == ' ' and (x, y) not in visited:
                    owner, territory = self.territory(x, y)
                    result[owner].update(territory)
                    visited.update(territory)
        
        return result