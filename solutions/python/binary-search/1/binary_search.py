def find(array, value):
    """
    Perform a binary search on a sorted array to find the given value.
    
    Args:
        array: A sorted list of elements
        value: The value to search for
    
    Returns:
        The index of the value in the array
    
    Raises:
        ValueError: If the value is not found in the array
    """
    if not array:
        raise ValueError("value not in array")
    
    left = 0
    right = len(array) - 1
    
    while left <= right:
        middle = (left + right) // 2
        
        if array[middle] == value:
            return middle
        
        if array[middle] > value:
            right = middle - 1
        else:
            left = middle + 1
    
    raise ValueError("value not in array")