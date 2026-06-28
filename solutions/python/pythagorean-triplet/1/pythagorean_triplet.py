def triplets_with_sum(n):
    triplets = []
    
    # Since a < b < c, 'a' can at most be slightly less than N // 3
    for a in range(1, n // 3):
        # Using the derived formula for b
        numerator = n**2 - 2 * n * a
        denominator = 2 * n - 2 * a
        
        # Check if b is a perfect integer
        if numerator % denominator == 0:
            b = numerator // denominator
            c = n - a - b
            
            # Ensure the strict ascending order condition holds
            if a < b < c:
                triplets.append([a, b, c])
                
    return triplets
