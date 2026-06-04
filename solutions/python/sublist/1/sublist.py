# Possible sublist categories.
SUBLIST = 1
SUPERLIST = 2
EQUAL = 3
UNEQUAL = 4


def is_contained_in(list_a, list_b):
    """Helper function to check if list_a is a sequential sublist of list_b."""
    if not list_a:
        return True
        
    len_a = len(list_a)
    len_b = len(list_b)
    
    for i in range(len_b - len_a + 1):
        if list_b[i:i + len_a] == list_a:
            return True
            
    return False


def sublist(list_one, list_two):
    # Case 1: Both lists are identical in length and elements
    if list_one == list_two:
        return EQUAL
        
    # Pre-calculate lengths to keep comparison syntax completely clean
    len_one = len(list_one)
    len_two = len(list_two)
        
    # Case 2: list_one is shorter, check if it's inside list_two
    if len_one < len_two:
        if is_contained_in(list_one, list_two):
            return SUBLIST
            
    # Case 3: list_one is longer, check if list_two is inside list_one
    elif len_one > len_two:
        if is_contained_in(list_two, list_one):
            return SUPERLIST
            
    # Case 4: No relationships match
    return UNEQUAL