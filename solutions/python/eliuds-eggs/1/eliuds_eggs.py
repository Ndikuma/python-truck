def egg_count(display_value):
    """
    Count the number of 1 bits by repeatedly dividing by 2.
    """
    count = 0
    
    while display_value > 0:
        # Check if odd (least significant bit is 1)
        if display_value % 2 == 1:
            count += 1
        
        # Divide by 2 to move to the next bit
        display_value //= 2
    
    return count