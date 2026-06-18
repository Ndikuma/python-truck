def slices(series, length):
    # Check for empty series
    if not series:
        raise ValueError("series cannot be empty")
    
    # Check for invalid length
    if length <= 0:
        raise ValueError("slice length cannot be zero" if length == 0 else "slice length cannot be negative")
    
    # Check if length exceeds series length
    if length > len(series):
        raise ValueError("slice length cannot be greater than series length")
    
    return [series[i:i + length] for i in range(len(series) - length + 1)]