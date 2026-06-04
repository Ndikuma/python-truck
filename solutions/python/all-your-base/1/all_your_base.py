def rebase(input_base, digits, output_base):
    # 1. Guard Clauses: Validate bases
    if input_base < 2:
        raise ValueError("input base must be >= 2")
    if output_base < 2:
        raise ValueError("output base must be >= 2")
        
    # 2. Guard Clauses & Step 1: Convert input digits to a Base-10 integer
    decimal_value = 0
    for digit in digits:
        if not 0 <= digit < input_base:
            raise ValueError("all digits must satisfy 0 <= d < input base")
        
        # Accumulate the value (Positional Notation)
        decimal_value = decimal_value * input_base + digit

    # 3. Handle edge case where the value evaluates to 0
    if decimal_value == 0:
        return [0]

    # 4. Step 2: Convert the Base-10 integer into the output_base
    output_digits = []
    while decimal_value > 0:
        # The remainder gives us the current lowest positional digit
        output_digits.append(decimal_value % output_base)
        # Divide by base to move to the next higher position
        decimal_value //= output_base

    # 5. The digits were gathered from right to left, so reverse them
    return output_digits[::-1]