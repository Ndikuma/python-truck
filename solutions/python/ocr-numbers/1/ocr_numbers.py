DIGIT_MAP = {
    " _ "
    "| |"
    "|_|"
    "   ": "0",
    
    "   "
    "  |"
    "  |"
    "   ": "1",
    
    " _ "
    " _|"
    "|_ "
    "   ": "2",
    
    " _ "
    " _|"
    " _|"
    "   ": "3",
    
    "   "
    "|_|"
    "  |"
    "   ": "4",
    
    " _ "
    "|_ "
    " _|"
    "   ": "5",
    
    " _ "
    "|_ "
    "|_|"
    "   ": "6",
    
    " _ "
    "  |"
    "  |"
    "   ": "7",
    
    " _ "
    "|_|"
    "|_|"
    "   ": "8",
    
    " _ "
    "|_|"
    " _|"
    "   ": "9"
}

def convert(input_grid):
    # 1. Handle input format (String vs List of strings)
    if isinstance(input_grid, str):
        if not input_grid:
            raise ValueError("Number of input lines is not a multiple of four")
        lines = input_grid.split('\n')
    elif isinstance(input_grid, list):
        if not input_grid:
            raise ValueError("Number of input lines is not a multiple of four")
        lines = input_grid
    else:
        raise ValueError("Invalid input type")
        
    # 2. Structural Validations
    if len(lines) % 4 != 0:
        raise ValueError("Number of input lines is not a multiple of four")
        
    line_length = len(lines[0])
    if line_length % 3 != 0:
        raise ValueError("Number of input columns is not a multiple of three")
        
    for line in lines:
        if len(line) != line_length:
            raise ValueError("Number of input columns is not a multiple of three")

    output_rows = []
    
    # 3. Process the grid 4 rows at a time
    for r in range(0, len(lines), 4):
        row_digits = []
        
        # Process 3 columns at a time
        for c in range(0, line_length, 3):
            cell_chars = (
                lines[r][c:c+3] +
                lines[r+1][c:c+3] +
                lines[r+2][c:c+3] +
                lines[r+3][c:c+3]
            )
            
            row_digits.append(DIGIT_MAP.get(cell_chars, "?"))
            
        output_rows.append("".join(row_digits))
        
    return ",".join(output_rows)