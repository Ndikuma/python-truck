def square_root(number):
    """
    Calculate the integer square root by sequential search.
    """
    if number <= 0:
        raise ValueError("Number must be positive")
    
    i = 1
    while i * i <= number:
        i += 1
    
    return i - 1