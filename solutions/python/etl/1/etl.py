def transform(legacy_data):
    """
    Transform the legacy scoring system from a one-to-many mapping
    to a one-to-one mapping with lowercase letters.
    
    Args:
        legacy_data: Dictionary where keys are point values and values are
                    lists of uppercase letters with that point value
    
    Returns:
        Dictionary where keys are lowercase letters and values are point values
    """
    new_data = {}
    
    # Iterate through each score and its list of letters
    for score, letters in legacy_data.items():
        # For each letter in the list, convert to lowercase and store with its score
        for letter in letters:
            new_data[letter.lower()] = score
    
    return new_data