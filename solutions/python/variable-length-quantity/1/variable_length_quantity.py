def encode(numbers):
    result = []
    
    for number in numbers:
        if number == 0:
            result.append(0x00)
            continue
        
        # Build bytes from most significant to least
        bytes_ = []
        while number > 0:
            bytes_.insert(0, number & 0x7F)
            number >>= 7
        
        # Set continuation bits
        for i in range(len(bytes_) - 1):
            bytes_[i] |= 0x80
        
        result.extend(bytes_)
    
    return result


def decode(bytes_):
    result = []
    current = 0
    last_byte = False
    
    for i, byte in enumerate(bytes_):
        current = (current << 7) | (byte & 0x7F)
        
        if (byte & 0x80) == 0:
            result.append(current)
            current = 0
            last_byte = True
    
    # Check if the last byte was a continuation byte
    if not last_byte or current != 0:
        raise ValueError("incomplete sequence")
    
    return result