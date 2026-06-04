def is_valid(isbn):
    # 1. Strip out the dashes
    cleaned = isbn.replace("-", "")
    
    # 2. An ISBN-10 must be exactly 10 characters long
    if len(cleaned) != 10:
        return False
        
    # 3. Validate characters and convert them to their numerical values
    digits = []
    for index, char in enumerate(cleaned):
        if char.isdigit():
            digits.append(int(char))
        # 'X' is only valid if it's the 10th character (index 9)
        elif char == 'X' and index == 9:
            digits.append(10)
        else:
            # Any other letter, or 'X' in the wrong position, makes it invalid
            return False

    # 4. Apply the ISBN-10 formula using a loop or zip
    # Coefficients go from 10 down to 1
    total = sum(d * (10 - i) for i, d in enumerate(digits))
    
    # 5. Check if it's perfectly divisible by 11
    return total % 11 == 0