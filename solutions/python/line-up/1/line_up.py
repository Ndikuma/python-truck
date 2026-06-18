def line_up(name, number):
    """
    Generate a ticket message with ordinal number for a customer.
    
    Args:
        name: Customer's name (string)
        number: Ticket number from 1 to 999 (integer)
    
    Returns:
        A formatted sentence with the customer's name and ordinal number
    """
    # Determine the ordinal suffix
    last_two_digits = number % 100
    last_digit = number % 10
    
    if 11 <= last_two_digits <= 13:
        suffix = "th"
    elif last_digit == 1:
        suffix = "st"
    elif last_digit == 2:
        suffix = "nd"
    elif last_digit == 3:
        suffix = "rd"
    else:
        suffix = "th"
    
    # Create the ordinal number string
    ordinal = f"{number}{suffix}"
    
    # Return the formatted sentence
    return f"{name}, you are the {ordinal} customer we serve today. Thank you!"