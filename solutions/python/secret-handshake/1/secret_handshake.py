def commands(binary_str):
    """
    Convert a binary string to secret handshake actions.
    
    For example:
        commands("00011") returns ["wink", "double blink"]
        commands("11010") returns ["jump", "double blink"]
    """
    
    # The handshake moves, in order from right to left
    handshake_moves = {
        0: "wink",
        1: "double blink", 
        2: "close your eyes",
        3: "jump"
    }
    
    # Make sure we have exactly 5 digits
    # Then reverse so we read from right to left
    bits = binary_str.zfill(5)[::-1]
    
    # Start with an empty list of moves
    my_moves = []
    
    # Look at each position (except the reverse bit at position 4)
    for position in range(4):
        if bits[position] == '1':
            my_moves.append(handshake_moves[position])
    
    # Check if we need to reverse everything
    # The 5th bit (position 4) means "reverse the order"
    if bits[4] == '1':
        my_moves.reverse()
    
    return my_moves