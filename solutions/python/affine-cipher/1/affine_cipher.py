import math

def _is_coprime(a, m):
    return math.gcd(a, m) == 1

def _mod_inverse(a, m):
    """Find modular inverse using the Extended Euclidean Algorithm."""
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    raise ValueError("Modular inverse does not exist.")

def encode(plain_text, a, b):
    if not _is_coprime(a, 26):
        raise ValueError("a and m must be coprime.")
    
    encoded_chars = []
    for char in plain_text.lower():
        if char.isalpha():
            x = ord(char) - ord('a')
            y = (a * x + b) % 26
            encoded_chars.append(chr(y + ord('a')))
        elif char.isdigit():
            encoded_chars.append(char)
            
    # Group into blocks of 5
    result = []
    for i in range(0, len(encoded_chars), 5):
        result.append("".join(encoded_chars[i:i+5]))
        
    return " ".join(result)

def decode(ciphered_text, a, b):
    if not _is_coprime(a, 26):
        raise ValueError("a and m must be coprime.")
    
    a_inv = _mod_inverse(a, 26)
    result = []
    
    for char in ciphered_text.lower():
        if char.isalpha():
            y = ord(char) - ord('a')
            # Ensure the result of (y - b) is positive before modulo
            x = (a_inv * (y - b)) % 26
            result.append(chr(x + ord('a')))
        elif char.isdigit():
            result.append(char)
            
    return "".join(result)