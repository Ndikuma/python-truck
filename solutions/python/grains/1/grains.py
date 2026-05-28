def square(number):
    """Calculate how many grains of wheat are on a specific chessboard square.

    :param number: int - the square number (1-64)
    :return: int - number of grains on that square
    """
    if not 1 <= number <= 64:
        raise ValueError("square must be between 1 and 64")
        
    return 2 ** (number - 1)


def total():
    """Calculate the total number of grains of wheat on the entire chessboard.

    :return: int - total number of grains
    """
    # The sum of 2^0 + 2^1 + ... + 2^63 is equal to (2^64) - 1
    return (2 ** 64) - 1