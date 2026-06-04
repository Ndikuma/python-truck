def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    # Guard clause with the exact error message expected by the test
    if number <= 0:
        raise ValueError("Classification is only possible for positive integers.")
        
    # Find all proper divisors and sum them up
    aliquot_sum = sum(i for i in range(1, (number // 2) + 1) if number % i == 0)
    
    # Classify the number
    if aliquot_sum == number:
        return "perfect"
    elif aliquot_sum > number:
        return "abundant"
    else:
        return "deficient"