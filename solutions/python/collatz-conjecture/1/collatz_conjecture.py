def steps(number):
    """Calculate the number of steps to reach 1 using the Collatz Conjecture.

    :param number: int - a positive integer
    :return: int - the number of steps to reach 1
    """
    if number <= 0:
        raise ValueError("Only positive integers are allowed")

    count = 0
    while number > 1:
        if number % 2 == 0:
            number = number // 2
        else:
            number = 3 * number + 1
        count += 1
        
    return count