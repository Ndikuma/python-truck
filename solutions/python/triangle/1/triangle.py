def is_valid_triangle(sides):
    """Check if the sides can form a valid triangle."""
    a, b, c = sides
    # All sides must have length > 0 and sum of any two sides must be >= the third
    return a > 0 and b > 0 and c > 0 and (a + b >= c) and (a + c >= b) and (b + c >= a)


def equilateral(sides):
    """Determine if a triangle is equilateral (all three sides are equal)."""
    return is_valid_triangle(sides) and len(set(sides)) == 1


def isosceles(sides):
    """Determine if a triangle is isosceles (at least two sides are equal)."""
    return is_valid_triangle(sides) and len(set(sides)) <= 2


def scalene(sides):
    """Determine if a triangle is scalene (all three sides have different lengths)."""
    return is_valid_triangle(sides) and len(set(sides)) == 3