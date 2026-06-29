def is_palindrome(number):
    """Check if a number is a palindrome."""
    s = str(number)
    return s == s[::-1]

def largest(min_factor, max_factor):
    """Find the largest palindrome product within the given range."""
    if min_factor > max_factor:
        raise ValueError("min must be <= max")
    
    max_product = None
    factors = []
    
    # Iterate downwards to find the largest product quickly
    for i in range(max_factor, min_factor - 1, -1):
        # Optimization: if i*i is already smaller than found max_product, break
        if max_product and i * max_factor < max_product:
            break
            
        for j in range(i, min_factor - 1, -1):
            product = i * j
            if max_product and product < max_product:
                break
            if is_palindrome(product):
                if product > (max_product or 0):
                    max_product = product
                    factors = [[j, i]]
                elif product == max_product:
                    factors.append([j, i])
                    
    return max_product, factors

def smallest(min_factor, max_factor):
    """Find the smallest palindrome product within the given range."""
    if min_factor > max_factor:
        raise ValueError("min must be <= max")
    
    min_product = None
    factors = []
    
    # Iterate upwards to find the smallest product quickly
    for i in range(min_factor, max_factor + 1):
        for j in range(i, max_factor + 1):
            product = i * j
            if min_product is not None and product > min_product:
                break
            if is_palindrome(product):
                if min_product is None or product < min_product:
                    min_product = product
                    factors = [[i, j]]
                elif product == min_product:
                    factors.append([i, j])
                    
    return min_product, factors