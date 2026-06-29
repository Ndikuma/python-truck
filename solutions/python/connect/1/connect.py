class ConnectGame:
    def __init__(self, board):
        # Normalize board input: split by newlines and handle indentation
        if isinstance(board, str):
            self.board = [line.strip() for line in board.strip().split('\n')]
        else:
            self.board = board
        self.height = len(self.board)
        # Determine width from the longest row
        self.width = max(len(row.replace(' ', '')) for row in self.board) if self.height > 0 else 0

    def get_winner(self):
        if self._has_connection('O', 'top', 'bottom'):
            return 'O'
        if self._has_connection('X', 'left', 'right'):
            return 'X'
        return ""

    def _get_cell(self, row, col):
        if row < 0 or row >= self.height or col < 0:
            return None
        row_data = self.board[row].replace(' ', '')
        return row_data[col] if col < len(row_data) else None

    def _get_neighbors(self, row, col, player):
        """Get valid neighbors belonging to the same player in a hex grid."""
        neighbors = []
        # For a skewed hex grid, the 6 neighbors are:
        # (row-1, col), (row-1, col+1), 
        # (row, col-1), (row, col+1), 
        # (row+1, col-1), (row+1, col)
        directions = [(-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0)]
        
        for dr, dc in directions:
            nr, nc = row + dr, col + dc
            if self._get_cell(nr, nc) == player:
                neighbors.append((nr, nc))
        return neighbors

    def _has_connection(self, player, start_side, end_side):
        """Check if a player has a connection from start_side to end_side."""
        start_positions = self._get_start_positions(player, start_side)
        
        for start in start_positions:
            visited = set()
            if self._dfs(start, player, end_side, visited):
                return True
        return False

    def _get_start_positions(self, player, side):
        positions = []
        if side == 'top':
            for col in range(self.width):
                if self._get_cell(0, col) == player:
                    positions.append((0, col))
        elif side == 'bottom':
            for col in range(self.width):
                if self._get_cell(self.height - 1, col) == player:
                    positions.append((self.height - 1, col))
        elif side == 'left':
            for row in range(self.height):
                if self._get_cell(row, 0) == player:
                    positions.append((row, 0))
        elif side == 'right':
            for row in range(self.height):
                if self._get_cell(row, self.width - 1) == player:
                    positions.append((row, self.width - 1))
        return positions

    def _dfs(self, pos, player, target_side, visited):
        if pos in visited:
            return False
        visited.add(pos)
        
        row, col = pos
        # Check if we've reached the target side
        if self._is_on_side(row, col, target_side):
            return True
        
        # Explore neighbors belonging to the same player
        for neighbor in self._get_neighbors(row, col, player):
            if self._dfs(neighbor, player, target_side, visited):
                return True
        return False

    def _is_on_side(self, row, col, side):
        if side == 'top': 
            return row == 0
        if side == 'bottom': 
            return row == self.height - 1
        if side == 'left': 
            return col == 0
        if side == 'right': 
            return col == self.width - 1
        return False