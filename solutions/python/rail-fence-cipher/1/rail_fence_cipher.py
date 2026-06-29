def encode(message, rails):
    """Encode a message using the Rail Fence cipher."""
    if rails <= 1:
        return message
    
    # Create the rail fence pattern
    fence = [[] for _ in range(rails)]
    row = 0
    direction = 1  # 1 for down, -1 for up
    
    # Place each character in the appropriate rail
    for char in message:
        fence[row].append(char)
        row += direction
        if row == rails - 1 or row == 0:
            direction = -direction
    
    # Read off the rails
    result = []
    for rail in fence:
        result.extend(rail)
    
    return ''.join(result)


def decode(encoded_message, rails):
    """Decode a message using the Rail Fence cipher."""
    if rails <= 1:
        return encoded_message
    
    # Determine the pattern of rail lengths
    # Create a pattern showing which rail each character belongs to
    pattern = []
    row = 0
    direction = 1
    
    for _ in range(len(encoded_message)):
        pattern.append(row)
        row += direction
        if row == rails - 1 or row == 0:
            direction = -direction
    
    # Count how many characters go on each rail
    rail_counts = [0] * rails
    for rail in pattern:
        rail_counts[rail] += 1
    
    # Split the encoded message into rails
    rails_data = []
    start = 0
    for count in rail_counts:
        rails_data.append(encoded_message[start:start + count])
        start += count
    
    # Reconstruct the message by reading the rails
    rail_positions = [0] * rails
    result = []
    
    for rail in pattern:
        char = rails_data[rail][rail_positions[rail]]
        result.append(char)
        rail_positions[rail] += 1
    
    return ''.join(result)