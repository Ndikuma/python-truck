def distance(strand_a, strand_b):
    """
    Calculate the Hamming distance between two DNA strands.
    
    The Hamming distance is the number of positions where the two strands differ.
    
    Args:
        strand_a: First DNA strand (string)
        strand_b: Second DNA strand (string)
    
    Returns:
        The number of differences between the strands
    
    Raises:
        ValueError: If the strands are not the same length
    """
    # Check if strands have the same length
    if len(strand_a) != len(strand_b):
        raise ValueError("Strands must be of equal length.")
    
    # Count the differences
    differences = 0
    for i in range(len(strand_a)):
        if strand_a[i] != strand_b[i]:
            differences += 1
    
    return differences