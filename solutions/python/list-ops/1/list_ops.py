def append(list1, list2):
    """Append all items in the second list to the end of the first list."""
    return list1 + list2


def concat(lists):
    """Combine a list of lists into a single flattened list."""
    flat_list = []
    for sublist in lists:
        flat_list += sublist
    return flat_list


def filter(function, input_list):
    """Filter list elements using a predicate function."""
    # Kept function name 'filter', but renamed parameter to 'input_list'
    return [item for item in input_list if function(item)]


def length(input_list):
    """Return the total number of items in a list."""
    count = 0
    for _ in input_list:
        count += 1
    return count


def map(function, input_list):
    """Apply a function to all elements in a list to produce a new list."""
    # Kept function name 'map', but renamed parameter to 'input_list'
    return [function(item) for item in input_list]


def foldl(function, input_list, initial):
    """Fold (reduce) a list from the left (start) to the right (end)."""
    accumulator = initial
    for item in input_list:
        accumulator = function(accumulator, item)
    return accumulator


def foldr(function, input_list, initial):
    """Fold (reduce) a list from the right (end) to the left (start)."""
    accumulator = initial
    # Process from right to left, passing (accumulator, item) to match the test setup
    for item in reversed(input_list):
        accumulator = function(accumulator, item)
    return accumulator


def reverse(input_list):
    """Reverse the elements of a list."""
    return input_list[::-1]