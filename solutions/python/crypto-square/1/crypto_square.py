import math

def cipher_text(plain_text):
    # 1. Normalize
    text = ''.join(ch for ch in plain_text.lower() if ch.isalnum())
    
    if not text:
        return ""
    
    # 2. Calculate dimensions
    length = len(text)
    cols = math.ceil(math.sqrt(length))
    rows = math.ceil(length / cols)
    
    # 3. Build grid with explicit padding to handle the trailing space requirement
    # Pad to ensure total size is rows * cols
    padded_text = text.ljust(rows * cols)
    
    chunks = []
    for col in range(cols):
        chunk = ""
        for row in range(rows):
            chunk += padded_text[row * cols + col]
        chunks.append(chunk)
    
    # Joining with space will leave the trailing space if the last chunk is space-padded
    return ' '.join(chunks)