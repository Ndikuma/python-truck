def rotate(text, key):
    result = []
    
    for char in text:
        # Check for lowercase letters
        if char.islower():
            # Shift character relative to 'a' (ASCII 97)
            shifted = (ord(char) - ord('a') + key) % 26 + ord('a')
            result.append(chr(shifted))
            
        # Check for uppercase letters
        elif char.isupper():
            # Shift character relative to 'A' (ASCII 65)
            shifted = (ord(char) - ord('A') + key) % 26 + ord('A')
            result.append(chr(shifted))
            
        # If it's a number, space, or punctuation, leave it exactly as it is
        else:
            result.append(char)
            
    # Glue the characters back together into a single string
    return "".join(result)