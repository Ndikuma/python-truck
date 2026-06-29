def largest_product(series, size):
    """Find the largest product of a contiguous series of digits of given size."""
    # Validate input
    if size < 0:
        raise ValueError("span must not be negative")
    
    if not series:
        if size == 0:
            return 1
        raise ValueError("span must not exceed string length")
    
    if size > len(series):
        raise ValueError("span must not exceed string length")
    
    if not series.isdigit():
        raise ValueError("digits input must only contain digits")
    
    # Handle empty series (size 0)
    if size == 0:
        return 1
    
    # Convert series to list of integers
    digits = [int(d) for d in series]
    
    # Find the maximum product
    max_product = 0
    for i in range(len(digits) - size + 1):
        product = 1
        for j in range(size):
            product *= digits[i + j]
        if product > max_product:
            max_product = product
    
    return max_product