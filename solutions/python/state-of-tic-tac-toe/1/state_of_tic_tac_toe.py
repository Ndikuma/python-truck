def gamestate(board):
    def winner(player):
        # rows
        for row in board:
            if all(cell == player for cell in row):
                return True

        # columns
        for col in range(3):
            if all(board[row][col] == player for row in range(3)):
                return True

        # diagonals
        if all(board[i][i] == player for i in range(3)):
            return True
        if all(board[i][2 - i] == player for i in range(3)):
            return True

        return False

    # flatten board
    flat = [cell for row in board for cell in row]

    x_count = flat.count("X")
    o_count = flat.count("O")

    # 1. turn validation
    if o_count > x_count:
        raise ValueError("Wrong turn order: O started")
    if x_count - o_count > 1:
        raise ValueError("Wrong turn order: X went twice")

    x_win = winner("X")
    o_win = winner("O")

    # 2. both win = invalid
    if x_win and o_win:
        raise ValueError("Impossible board: game should have ended after the game was won")

    # 3. X wins but extra moves played
    if x_win and x_count != o_count + 1:
        raise ValueError("Wrong turn order: X went twice")

    # 4. O wins but wrong move count
    if o_win and x_count != o_count:
        raise ValueError("Wrong turn order: O started")

    # 5. win state
    if x_win or o_win:
        return "win"

    # 6. draw
    if all(cell in ["X", "O"] for cell in flat):
        return "draw"

    # 7. ongoing
    return "ongoing"