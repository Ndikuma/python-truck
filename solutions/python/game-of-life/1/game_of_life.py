def tick(matrix):
    rows = len(matrix)
    cols = len(matrix[0]) if rows > 0 else 0
    
    # Create a new blank matrix filled with 0s
    next_matrix = [[0] * cols for _ in range(rows)]
    
    for r in range(rows):
        for c in range(cols):
            # Count live neighbors in the 3x3 grid around the cell
            live_neighbors = 0
            for i in (-1, 0, 1):
                for j in (-1, 0, 1):
                    if i == 0 and j == 0: 
                        continue
                    
                    nr, nc = r + i, c + j
                    if 0 <= nr < rows and 0 <= nc < cols and matrix[nr][nc] == 1:
                        live_neighbors += 1
            
            # Apply Game of Life rules
            if matrix[r][c] == 1 and (live_neighbors == 2 or live_neighbors == 3):
                next_matrix[r][c] = 1  # Survives
            elif matrix[r][c] == 0 and live_neighbors == 3:
                next_matrix[r][c] = 1  # Born
                
    return next_matrix