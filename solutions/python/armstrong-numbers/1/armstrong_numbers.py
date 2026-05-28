def is_armstrong_number(number):
    digits_str = str(number)
    num_digits = len(digits_str)
    
    # Sum each digit raised to the power of the total number of digits
    armstrong_sum = sum(int(digit) ** num_digits for digit in digits_str)
    
    return armstrong_sum == number
