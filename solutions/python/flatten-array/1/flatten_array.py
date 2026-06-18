def flatten(items):
    """
    Flatten a nested array of any depth.
    
    This function recursively traverses the input array, extracting all
    non-null values into a single flat array.
    
    Args:
        items: A nested array (list) of any depth
        
    Returns:
        A flat array containing all non-null values from the input
    """
    result = []
    
    for item in items:
        # If the item is a list, recursively flatten it
        if isinstance(item, list):
            result.extend(flatten(item))
        # If the item is not None, add it to the result
        elif item is not None:
            result.append(item)
        # None values are skipped (excluded)
    
    return result