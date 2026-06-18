def two_fer(name=None):
    """
    Generate a two-fer message for giving away a cookie.
    
    Args:
        name: The name of the person receiving the extra cookie (optional)
    
    Returns:
        A string with the appropriate two-fer dialogue
    """
    if name is None:
        return "One for you, one for me."
    else:
        return f"One for {name}, one for me."