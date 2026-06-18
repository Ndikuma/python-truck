from datetime import datetime, timedelta

def add(birth_date):
    """
    Calculate the date and time one gigasecond after the given birth date.
    
    A gigasecond is exactly 1,000,000,000 seconds.
    
    Args:
        birth_date: A datetime object representing the birth date and time
    
    Returns:
        A datetime object representing the date and time one gigasecond later
    """
    # A gigasecond is 1,000,000,000 seconds
    # Create a timedelta with that many seconds
    gigasecond = timedelta(seconds=1_000_000_000)
    
    # Add the gigasecond to the birth date
    return birth_date + gigasecond