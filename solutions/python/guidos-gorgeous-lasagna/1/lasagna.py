EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2

def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    Parameters:
        elapsed_bake_time (int): The baking time already elapsed.

    Returns:
        int: The remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time

def preparation_time_in_minutes(number_of_layers):
    """Calculate the preparation time.

    Parameters:
        number_of_layers (int): The number of layers in the lasagna.

    Returns:
        int: The total preparation time (in minutes) derived from 'PREPARATION_TIME'.

    Function that takes the number of layers you want to make and returns
    how many minutes you would spend making them based on the `PREPARATION_TIME`.
    """
    return PREPARATION_TIME * number_of_layers

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the total elapsed time.

    Parameters:
        number_of_layers (int): The number of layers in the lasagna.
        elapsed_bake_time (int): The baking time already elapsed.

    Returns:
        int: The total elapsed time (in minutes) calculated as preparation time plus bake time.

    Function that takes the number of layers and the elapsed baking time as
    arguments and returns the total elapsed time (preparation + baking).
    """
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time