def encode(plain_text):
    ciphered_chars = []
    
    for char in plain_text.lower():
        if char.isalpha():
            # Atbash mirror math ('a' is ASCII 97)
            ciphered_chars.append(chr(97 + (25 - (ord(char) - 97))))
        elif char.isdigit():
            # Numbers are left unchanged
            ciphered_chars.append(char)
        # Punctuation and spaces are implicitly excluded
            
    # Join into chunks of 5 characters separated by a space
    result = []
    for i in range(0, len(ciphered_chars), 5):
        result.append("".join(ciphered_chars[i:i+5]))
        
    return " ".join(result)


def decode(ciphered_text):
    # Strip spaces to remove the 5-letter grouping formatting
    clean_text = ciphered_text.replace(" ", "")
    result = ""
    
    for char in clean_text:
        if char.isalpha():
            # Atbash is symmetric, so decoding uses the exact same mirror logic
            result += chr(97 + (25 - (ord(char) - 97)))
        else:
            result += char
            
    return result