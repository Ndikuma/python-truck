import random
import string

class Cipher:
    def __init__(self, key=None):
        """Initialize the cipher with a key."""
        if key is None:
            # Generate a random key of 100 lowercase letters
            self.key = ''.join(random.choice(string.ascii_lowercase) for _ in range(100))
        else:
            # Ensure the key contains only lowercase letters
            if not key.islower() or not key.isalpha():
                raise ValueError("Key must contain only lowercase letters")
            self.key = key

    def encode(self, text):
        """Encode the plaintext using the Vigenère cipher."""
        return self._transform(text, 1)

    def decode(self, text):
        """Decode the ciphertext using the Vigenère cipher."""
        return self._transform(text, -1)

    def _transform(self, text, direction):
        """Transform text using the key and direction (1 for encode, -1 for decode)."""
        result = []
        key_index = 0
        
        for char in text:
            if char.isalpha():
                # Get shift value from key (a=0, b=1, ..., z=25)
                shift = ord(self.key[key_index % len(self.key)]) - ord('a')
                key_index += 1
                
                # Apply the shift (encode: +shift, decode: -shift)
                if char.isupper():
                    base = ord('A')
                    shifted = (ord(char) - base + direction * shift) % 26
                    result.append(chr(base + shifted))
                else:  # lowercase
                    base = ord('a')
                    shifted = (ord(char) - base + direction * shift) % 26
                    result.append(chr(base + shifted))
            else:
                # Non-alphabetic characters are preserved
                result.append(char)
        
        return ''.join(result)
