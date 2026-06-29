def rectangles(strings):
    """Count the number of rectangles in an ASCII diagram."""
    if not strings:
        return 0
    
    height = len(strings)
    width = len(strings[0])
    
    # Find all corners ('+') positions
    corners = []
    for row in range(height):
        for col in range(width):
            if strings[row][col] == '+':
                corners.append((row, col))
    
    count = 0
    
    # Check each pair of corners as potential top-left and bottom-right
    for i in range(len(corners)):
        r1, c1 = corners[i]  # top-left corner
        for j in range(i + 1, len(corners)):
            r2, c2 = corners[j]  # bottom-right corner
            
            # Must be a valid rectangle: r1 < r2 and c1 < c2
            if r1 >= r2 or c1 >= c2:
                continue
            
            # Check if the other two corners exist
            if (r1, c2) not in corners or (r2, c1) not in corners:
                continue
            
            # Check top edge: from (r1, c1) to (r1, c2)
            valid = True
            for col in range(c1 + 1, c2):
                if strings[r1][col] not in '+-':
                    valid = False
                    break
            if not valid:
                continue
            
            # Check bottom edge: from (r2, c1) to (r2, c2)
            for col in range(c1 + 1, c2):
                if strings[r2][col] not in '+-':
                    valid = False
                    break
            if not valid:
                continue
            
            # Check left edge: from (r1, c1) to (r2, c1)
            for row in range(r1 + 1, r2):
                if strings[row][c1] not in '+|':
                    valid = False
                    break
            if not valid:
                continue
            
            # Check right edge: from (r1, c2) to (r2, c2)
            for row in range(r1 + 1, r2):
                if strings[row][c2] not in '+|':
                    valid = False
                    break
            if not valid:
                continue
            
            count += 1
    
    return count